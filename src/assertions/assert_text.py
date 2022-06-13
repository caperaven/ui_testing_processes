from src.elements import get_element
from src.errors import set_error
from src.utils import get_name


async def assert_text_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.text
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: text on '{}' should have been '{}' but was '{}'".format(name, exp_value, value))


async def assert_text_neq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.text
    exp_value = args["value"]

    if value == exp_value:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: text on '{}' should have been '{}' but was '{}'".format(name, exp_value, value))
    else:
        results[args["step"]] = "success"
