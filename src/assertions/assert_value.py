from src.elements import get_element
from src.errors import set_error


async def assert_value_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    exp_value = args["value"]
    value = element.get_attribute("value")

    if str(exp_value) == str(value):
        results[args["step"]] = "success"
    else:
        await set_error(driver, results, args["step"], "error: expected {} but found {}".format(exp_value, value))


async def assert_value_neq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    exp_value = args["value"]
    value = element.get_attribute("value")

    if value is None:
        return

    if str(exp_value) == str(value):
        await set_error(driver, results, args["step"], "error: value should not be {}".format(value))
    else:
        results[args["step"]] = "success"
