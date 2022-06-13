from selenium import webdriver
from src.action_systems.assert_actions import AssertActions
from src.action_systems.wait_actions import WaitActions
from src.action_systems.perform_actions import PerformActions
from src.schema_registry import SchemaRegistry
from src.process_runner import ProcessRunner
import asyncio
import sys


class Api:
    @property
    def current_step(self):
        return self.current["step"]

    def __init__(self):
        self.process_schema_registry = SchemaRegistry()
        self.process = ProcessRunner()
        self.intent = {
            "assert": AssertActions,
            "wait": WaitActions,
            "perform": PerformActions
        }
        self.current = {
            "schema": None,
            "process": None,
            "step": None
        }

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
            await self.process.run_process(self, None, process,  item, parameters)
        else:
            system = self.intent[system]
            fn = getattr(system, fn)
            return await fn({"args": args}, self, process, item)

    async def run_all(self):
        while schema := self.process_schema_registry.get_next_schema():
            await self.process.run(schema, self)

    def close(self):
        self.driver.close()


crs = Api()
asyncio.run(crs.run_all())
crs.close()