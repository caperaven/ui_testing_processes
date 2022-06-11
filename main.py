from src.action_systems.assert_actions import AssertActions
from src.action_systems.wait_actions import WaitActions
from src.action_systems.perform_actions import PerformActions
from src.schema_registry import SchemaRegistry
from src.process_runner import ProcessRunner


class Api:
    def __init__(self):
        self.processSchemaRegistry = SchemaRegistry()
        self.process = ProcessRunner()
        self.intent = {
            "assert": AssertActions,
            "wait": WaitActions,
            "perform": PerformActions
        }

    def call(self, system, fn, args, context, process, item):
        return self.intent[system][fn]({args: args}, context, process, item)


crs = Api()

ctx = {}
crs.process.set_value("$context.subobj.value", 10, ctx)
result = crs.process.get_value("$context.subobj.value", ctx)
print(result)
print(ctx)
