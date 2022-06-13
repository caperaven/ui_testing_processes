import time

from selenium.common.exceptions import StaleElementReferenceException

from src.elements import get_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from src.errors import set_error
from src.utils import get_name
from src.wait.conditions import _is_enabled_condition


async def click(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        WebDriverWait(driver, 10).until(_is_enabled_condition(args, results))

        action_key_down = None
        action_key_up = None

        if args.keys().__contains__("ctrl"):
            action_key_down = ActionChains(driver).key_down(Keys.CONTROL)

        if args.keys().__contains__("alt"):
            action_key_up = ActionChains(driver).key_up(Keys.CONTROL)

        if action_key_down:
            action_key_down.perform()

        element.click()

        if action_key_up:
            action_key_up.perform()

        results[args["step"]] = "success"
    except StaleElementReferenceException:
        time.sleep(0.25)
        await click(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: element '{}' not clickable, '{}'".format(name, e))
        pass


async def dbl_click(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        action = ActionChains(driver).double_click(element)
        action.perform()
        results[args["step"]] = "success"
    except StaleElementReferenceException:
        time.sleep(0.25)
        await dbl_click(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: element '{}' not dbl clickable, '{}'".format(name, e))
        pass


async def context_click(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        action = ActionChains(driver).context_click(element)
        action.perform()
        results[args["step"]] = "success"
    except StaleElementReferenceException:
        time.sleep(0.25)
        await context_click(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: element '{}' not context clickable, '{}'".format(name, e))
        pass


async def click_sequence(driver, args, results):
    sequence = args.sequence
    for query in sequence:
        await click(driver, {"query": query}, results)