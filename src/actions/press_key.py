import time
from selenium.common.exceptions import StaleElementReferenceException
from src.elements import get_element
from src.errors import set_error
from src.utils import get_name
from selenium.webdriver.common.keys import Keys


async def press_key(driver, args, results):
    try:
        element = get_element(driver, args, results)

        if element is None:
            return

        key_value = args["key"]
        key = getattr(Keys, key_value)
        element.send_keys(key)
    except StaleElementReferenceException:
        time.sleep(0.25)
        await press_key(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: could not press key '{}' on '{}', message: '{}'".format(args["key"], name, e))
        pass