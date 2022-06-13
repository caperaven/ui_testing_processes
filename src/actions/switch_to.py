import time

from selenium.common.exceptions import StaleElementReferenceException

from src.errors import set_error
from src.elements import get_element
from src.utils import get_name


async def switch_to_frame(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        driver.switch_to.frame(element)
    except StaleElementReferenceException:
        time.sleep(0.25)
        await switch_to_frame(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: could not switch to frame '{}', '{}'".format(name, e))
        pass


async def switch_to_default(driver, args, results):
    try:
        driver.switch_to.default_content()
    except StaleElementReferenceException:
        time.sleep(0.25)
        await switch_to_default(driver, args, results)
        pass
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: could not switch to default content, '{}'".format(e))
        pass


async def switch_to_tab(driver, args, results):
    try:
        time.sleep(1)
        index = args["index"]
        driver.switch_to.window(driver.window_handles[index])
    except StaleElementReferenceException:
        time.sleep(0.25)
        await switch_to_tab(driver, args, results)
        pass
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: could not swap to tab ({}), {}".format(index, e))
        pass
