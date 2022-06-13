class ProcessRunner:
    async def run(self, schema, api, context=None):
        main = schema["main"]
        await self.run_process(api, context, main, None, None)

    async def run_process(self, api, context, process, item, parameters):
        if "parameters_def" in process:
            success = copy_parameters(process, parameters)
            if success is not True:
                api.log_error(success)

        start = process["steps"]["start"]
        api.current["step"] = "start"
        await self.run_step(api, start, context, process, item)

    async def run_step(self, api, step, context, process, item):
        step_type = step["type"]
        step_action = step["action"]
        step_args = step["args"]

        await api.call(step_type, step_action, step_args, context, process, item)

        if "next_step" in step:
            next_step_name = step["next_step"]
            next_step = process["steps"][next_step_name]
            api.current["step"] = next_step_name
            await self.run_step(api, next_step, context, process, item)

    def get_value(self, expr, context, process=None, item=None):
        if not isinstance(expr, str): return expr
        if expr.__contains__("${"): return expr
        if expr == "$context": return context
        if expr == "$process": return process
        if expr == "$item": return item
        if not expr.__contains__("$"): return expr

        obj = context
        if expr.__contains__("$process"): obj = process
        if expr.__contains__("$item"): obj = item

        parts = expr.split(".")
        del parts[0]
        return get_value_on_path(obj, parts)

    def set_value(self, expr, value, context, process=None, item=None):
        obj = context
        if expr.__contains__("$process"): obj = process
        if expr.__contains__("$item"): obj = item

        parts = expr.split(".")
        del parts[0]
        obj = ensure_path(obj, parts)
        prop = parts[0]
        obj[prop] = value
        pass


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
    value = obj[property]
    del parts[0]

    if len(parts) == 0:
        return value
    else:
        return get_value_on_path(value, parts)


def ensure_path(obj, parts):
    if len(parts) == 1:
        return obj

    prop = parts[0]
    if hasattr(obj, prop) is False or obj[prop] is None:
        obj[prop] = {}
        del parts[0]
        return ensure_path(obj[prop], parts)
