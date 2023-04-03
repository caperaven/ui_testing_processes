from src.data import state
from src.errors import set_error
from src.logger import Logger
from src.memory import get_memory
import traceback


class ProcessRunner:
    async def run(self, schema, context=None):
        if "sequences" in schema:
            result = {}
            sequences = schema["sequences"]
            for sequence in sequences:
                process_name = sequence["process"]
                process = schema[process_name].copy()

                process["_results"] =  {}

                Logger.test_started("{} {}".format(schema["name"], sequence["process"]))
                await self.run_process(context, process, None, None)
                Logger.test_finished("{} {}".format(schema["name"], sequence["process"]))

                result[process_name] = process["_results"]

            return result
        else:
            main = schema["main"].copy()
            main["_results"] = {}

            Logger.test_started(schema["name"])
            await self.run_process(context, main, None, None)
            Logger.test_finished(schema["name"])

            return {"main": main["_results"]}

    async def run_process(self, context, process, item, parameters):
        if "parameters_def" in process:
            success = copy_parameters(process, parameters)
            if success is not True:
                await set_error(context.driver, process["_results"], "parameters_required", success)

        process["_results"]["memory"] = {
            "start": get_memory(context.driver, 1),
        }

        start = process["steps"]["start"]

        if "data" not in process:
            process["data"] = {}

        try:
            process["current_step"] = "start"
            await self.run_step(start, context, process, item)

            process["_results"]["memory"]["end"] = get_memory(context.driver, 1)
        except Exception as e:
            print(traceback.format_exc())
            message = "internal error: {}".format(e)
            await set_error(context.driver, process["_results"], process["current_step"], message)

    async def run_step(self, step, context, process, item):
        step_type = step["type"]
        step_action = step["action"]
        step_args = step["args"].copy() if "args" in step else {}

        parse_id(step_args, context, process, item)
        parse_args(step_args, context, process, item)

        step_args["step"] = process["current_step"]
        await context.call(step_type, step_action, step_args, context, process, item)

        if "next_step" in step:
            next_step_name = step["next_step"]
            process["current_step"] = next_step_name
            next_step = process["steps"][next_step_name]
            await self.run_step(next_step, context, process, item)

    def get_value(self, expr, context, process=None, item=None):
        if not isinstance(expr, str): return expr

        if expr.__contains__("${"):
            return get_formatted_text(expr, context, process, item)

        if expr == "$context": return context
        if expr == "$process": return process
        if expr == "$item": return item
        if not expr.__contains__("$"): return expr

        expr = expr.replace("$parameters", "$process.parameters")

        obj = context
        if expr.__contains__("$process"): obj = process
        if expr.__contains__("$item"): obj = item
        if expr.__contains__("$state"): obj = state
        if expr.__contains__("$data"): obj = process["data"]

        parts = expr.split(".")
        del parts[0]
        return get_value_on_path(obj, parts)

    def set_value(self, expr, value, context, process=None, item=None):
        obj = context
        if expr.__contains__("$process"): obj = process
        if expr.__contains__("$item"): obj = item
        if expr.__contains__("$state"): obj = state
        if expr.__contains__("$data"): obj = process["data"]

        parts = expr.split(".")
        del parts[0]
        obj = ensure_path(obj, parts)
        prop = parts[0]
        obj[prop] = value
        pass

def get_formatted_text(expr, context, process, item):
    parts = expr.split("${")

    buffer = []
    for part in parts:
        if "}" in part:
            index = part.index("}")
            path = "${}".format(part[0:index])

            convert_type = None
            if ":number" in path:
                convert_type = "number"
                path = path.replace(":number", "")

            if ":boolean" in path:
                convert_type = "boolean"
                path = path.replace(":boolean", "")

            value = context.get_value(path, context, process, item)

            if convert_type == "number":
                return int(value)

            if convert_type == "boolean":
                return bool(value)

            buffer.append("{}{}".format(value, part[index + 1:]))
            pass
        else:
            buffer.append(part)

    return ''.join(buffer)

def copy_parameters(process, parameters):
    if parameters is None:
        return "error: parameters required"

    process["parameters"] = parameters.copy()

    definitions = process["parameters_def"]
    keys = process["parameters_def"].keys()

    for key in keys:
        definition = definitions[key]
        if "required" in definition and definition["required"] == True:
            if not key in parameters:
                return 'parameter "{}" required'.format(key)

    return True


def get_value_on_path(obj, parts):
    if obj is None: return None

    property = parts[0]

    value = None
    if property in obj:
        value = obj[property]
    else:
        return value

    del parts[0]

    if len(parts) == 0:
        return value
    else:
        return get_value_on_path(value, parts)


def ensure_path(obj, parts):
    if len(parts) == 1:
        return obj

    prop = parts[0]
    if prop in obj is False or obj[prop] is None:
        obj[prop] = {}

    del parts[0]
    return ensure_path(obj[prop], parts)

def parse_id(args, context, process, item):
    if "query" in args:
        args["query"] = context.get_value(args["query"], context, process, item)
    elif "id" in args:
        args["id"] = context.get_value(args["id"], context, process, item)

def parse_args(args, context, process, item):
    keys = args.keys()

    for key in keys:
        if key == "id" or key == "query":
            continue

        value = context.get_value(args[key], context, process, item)
        args[key] = value
