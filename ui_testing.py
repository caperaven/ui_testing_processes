from selenium import webdriver
from src.action_systems.assert_actions import AssertActions
from src.action_systems.wait_actions import WaitActions
from src.action_systems.perform_actions import PerformActions
from src.action_systems.system_actions import SystemActions
from src.schema_registry import SchemaRegistry
from src.process_runner import ProcessRunner
from src.data import state
from src.results_writer import save_results, set_results_folder
import asyncio
import sys
import tempfile
import subprocess

from src.test_scraper import TestScraper

folder = tempfile.gettempdir()
set_results_folder(folder)

class Api:
    @property
    def get_value(self):
        return self.process.get_value

    @property
    def set_value(self):
        return self.process.set_value

    def __init__(self):
        self.process_schema_registry = SchemaRegistry()
        self.process = ProcessRunner()
        self.scraper = TestScraper()

        self.intent = {
            "assert": AssertActions,
            "wait": WaitActions,
            "perform": PerformActions,
            "system": SystemActions
        }

        self.current = {
            "schema": None,
            "process": None,
            "step": None
        }

        self.results = {
        }

        self.previous_result = None

        if sys.platform == "darwin":
            self.driver = webdriver.Safari()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("ignore-certificate-errors")

            if sys.argv.__contains__("--debug"):
                options.add_argument("-disable-extensions")
                options.add_argument("--auto-open-devtools-for-tabs")
                options.add_argument("--enable-precise-memory-info")
                options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=options)

    async def call(self, system, fn, args, context, process, item):
        system = self.intent[system]
        fn = getattr(system, fn)
        return await fn({"args": args}, self, process, item)

    async def run_all(self):
        while schema := self.process_schema_registry.get_next_schema():
            self.current["schema"] = schema
            id = schema["id"]
            self.results[id] = {
                "summary": {
                    "success": True,
                    "error_count": 0
                }
            }

            result = await self.process.run(schema, self)
            keys = result.keys()

            for key in keys:
                self.results[id][key] = result[key]

            calculate_success(self.results[id])

    async def run_process(self, args, context, parent_process, item):
        process_name = args["process"]
        process = self.current["schema"][process_name].copy()
        process["_results"] = {}
        process["parent_step"] = parent_process["current_step"]
        process["current_step"] = "start"

        parameters = args["parameters"].copy() if "parameters" in args else None

        if parameters is not None:
            keys = parameters.keys()
            for key in keys:
                value = parameters[key]
                new_value = context.get_value(value, context, parent_process, item)
                parameters[key] = new_value

        await self.process.run_process(context, process, None, parameters)

        return process

    def close(self):
        save_results(self.results)
        self.driver.close()

def calculate_success(results):
    error_count = count_errors(0, results)
    results["summary"]["error_count"] = error_count

    if error_count > 0:
        results["summary"]["success"] = False
    pass

def count_errors(count, obj):
    keys = obj.keys()

    result = 0
    for key in keys:
        value = obj[key]

        if type(value) is str and "error:" in value:
            result += 1

        if type(value) is dict:
            result += count_errors(count, value)

    return result
    pass

try:
    crs = Api()
    asyncio.run(crs.run_all())
except Exception as e:
    print(e)
finally:
    crs.close()

    if "--auto-open" in sys.argv:
        path = state["folder"]
        subprocess.Popen(r'explorer /open,"{}"'.format(path))
        pass