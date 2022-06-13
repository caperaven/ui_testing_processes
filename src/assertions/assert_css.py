from src.elements import get_element
from src.errors import set_error
from src.utils import get_name


async def assert_style_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    prop = args['property']
    value = element.value_of_css_property(prop)
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: css property '{}' on '{}' should have been '{}' but was '{}'".format(prop, name, exp_value, value))


async def assert_style_neq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    prop = args['property']
    value = element.value_of_css_property(prop)
    exp_value = args["value"]

    if value == exp_value:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: css property '{}' on '{}' should NOT have been '{}'".format(prop, name, exp_value, value))
    else:
        results[args["step"]] = "success"
