from src.elements import get_element
from src.errors import set_error
from src.utils import get_name


async def assert_attributes(driver, args, results):
    element = get_element(driver, args, results)
    attributes = args["attributes"]

    name = get_name(args)
    success = True
    for attr in attributes:
        exp_value = attributes[attr]
        value = element.get_attribute(attr)

        if value != exp_value:
            success = False
            await set_error(driver, results, args["step"],
                "error: attribute '{}' on '{}' should have been '{}' but was '{}'".format(attr, name, exp_value, value))
            break

    if success:
        results[args["step"]] = "success"


async def assert_attr_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: attribute '{}' on '{}' should have been '{}' but was '{}'".format(args["attr"], name, exp_value, value))


async def assert_attr_nq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: attribute '{}' on '{}' should NOT have been '{}'".format(args["attr"], name, exp_value))
    else:
        results[args["step"]] = "success"
