from selenium.webdriver.support.color import Color


def get_name(args):
    if "id" in args:
        return args["id"]

    if "query" in args:
        return args["query"]


def get_eval(args):
    if "eval" in args:
        return args["eval"]
    else:
        return None


def has_shadow_root(element):
    result = True
    try:
        root = element.shadow_root
        if root is None:
            result = False
    except Exception as e:
        result = False

    return result


def update_args_value(step, context, process, item, key):
    args = step["args"]
    value = args[key]
    value = context.process.get_value(value, context, process, item)
    args[key] = value
    step["args"] = args

def rgba_to_hex(rgba_value):
    color = Color.from_string(rgba_value)
    return color.hex


# css_value_format
def css_value_formatter(value):
    """
    convert a specific css value to an assertable value
    for example: finds rgba in this value string and convert it to HEX
    example : rgba(0, 0, 0, 1)  => #000000
    example: margin(0 0) => margin(0 0 0 0)
    """
