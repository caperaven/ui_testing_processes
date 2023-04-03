from src.elements import get_element
from src.errors import set_error
from src.utils import get_name
from src.memory import get_memory

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
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }


async def assert_attr_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: attribute '{}' on '{}' should have been '{}' but was '{}'".format(args["attr"], name, exp_value, value))


async def assert_attr_neq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: attribute '{}' on '{}' should NOT have been '{}'".format(args["attr"], name, exp_value))
    else:
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }

async def assert_has_attr(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])

    if value is None:
        await set_error(driver, results, args["step"], "error: has_attribute '{}' should exist but does not".format(args["attr"]))
    else:
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }

async def assert_has_not_attr(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])

    if value is None:
        value = ""

    if len(value) > 0:
        await set_error(driver, results, args["step"], "error: has_attribute '{}' should not exist but does on '{}'".format(args["attr"], args["query"]))
    else:
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }

async def assert_has_class(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    exp_value = exp_value = args["value"]
    value = element.get_attribute(args["attr"])

    if value is not None and value.__contains__(exp_value):
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }
    else:
        await set_error(driver, results, args["step"], "error: expected class '{}' to exist on '{}'".format(exp_value, query))


async def assert_has_not_class(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    exp_value = exp_value = args["value"]
    value = element.get_attribute(args["attr"])

    if value is not None and value.__contains__(exp_value):
        await set_error(driver, results, args["step"], "error: expected class '{}' to NOT exist on '{}'".format(exp_value, query))
    else:
        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }

