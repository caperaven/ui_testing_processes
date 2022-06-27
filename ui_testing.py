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

folder = tempfile.gettempdir()
set_results_folder(folder)

class Api:
    @property
    def current_step(self):
        return self.current["step"]

    @property
    def get_value(self):
        return self.process.get_value

    @property
    def set_value(self):
        return self.process.set_value

    def __init__(self):
        self.process_schema_registry = SchemaRegistry()
        self.process = ProcessRunner()
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

        self.current_result = None
        self.previous_result = None

        if sys.platform == "darwin":
            self.driver = webdriver.Safari()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")

            if sys.argv.__contains__("--debug"):
                options.add_argument("-disable-extensions")
                options.add_argument("--auto-open-devtools-for-tabs")
                options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=options)

    async def call(self, system, fn, args, context, process, item):
        if system == "process":
            schema = args["schema"]
            self.current["schema"] = str(schema)
            schema = self.process_schema_registry.get_template(schema)
            self.current["process"] = fn
            process = schema[fn]
            parameters = None if "parameters" not in args else args["parameters"]

            id = schema["id"]
            key = "{} -> {} template".format(self.current["step"], id)

            self.current_result[key]= {
                "summary": {
                    "success": True,
                    "error_count": 0
                }
            }

            self.previous_result = self.current_result
            self.current_result = self.current_result[key]

            await self.process.run_process(self, None, process,  item, parameters)
            self.current_result = self.previous_result
            self.previous_result = None
        else:
            system = self.intent[system]
            fn = getattr(system, fn)
            return await fn({"args": args}, self, process, item)

    async def run_all(self):
        while schema := self.process_schema_registry.get_next_schema():
            id = schema["id"]
            self.results[id] = {
                "summary": {
                    "success": True,
                    "error_count": 0
                }
            }

            self.current_result = self.results[id]
            await self.process.run(schema, self)

    def close(self):
        save_results(self.results)
        self.driver.close()


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