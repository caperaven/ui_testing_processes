from src.evaluate import clean_exp


class ProcessRunner:
    def run(self):
        pass

    def run_step(self):
        pass

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
