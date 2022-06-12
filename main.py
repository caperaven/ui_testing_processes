from src.action_systems.assert_actions import AssertActions
from src.action_systems.wait_actions import WaitActions
from src.action_systems.perform_actions import PerformActions
from src.schema_registry import SchemaRegistry
from src.process_runner import ProcessRunner
import asyncio

class Api:
    def __init__(self):
        self.process_schema_registry = SchemaRegistry()
        self.process = ProcessRunner()
        self.intent = {
            "assert": AssertActions,
            "wait": WaitActions,
            "perform": PerformActions
        }

    async def call(self, system, fn, args, context, process, item):
        return self.intent[system][fn]({args: args}, context, process, item)

    async def run_all(self):
        while schema := self.process_schema_registry.get_next_schema():
            await self.process.run(schema)


crs = Api()
asyncio.run(crs.run_all())