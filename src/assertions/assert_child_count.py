from src.errors import set_error
from src.utils import get_name


async def assert_child_count_eq(driver, args, results):
    query = "{} *".format(args["query"])
    count = args["count"]

    all_children_by_css = driver.find_elements_by_css_selector(query)
    act_count = len(all_children_by_css)

    if act_count == count:
        results[args["step"]] = "success"
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: child count on '{}' should have been '{}' but was '{}'".format(name, count, act_count))


async def assert_child_count_neq(driver, args, results):
    query = "{} *".format(args["query"])
    count = args["count"]

    all_children_by_css = driver.find_elements_by_css_selector(query)
    act_count = len(all_children_by_css)

    if act_count != count:
        results[args["step"]] = "success"
    else:
        name = get_name(args)
        await set_error(driver, results, args["step"],
                  "error: child count on '{}' should NOT have been '{}' but was".format(name, count))
