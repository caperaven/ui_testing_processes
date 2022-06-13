import time
from selenium.common.exceptions import StaleElementReferenceException
from src.elements import get_element
from src.errors import set_error
from src.utils import get_name
from selenium.webdriver.support.ui import Select


async def select_option(driver, args, results):
    try:
        element = get_element(driver, args, results)

        if element is None:
            return

        select = Select(element)
        select.select_by_value(args["value"])
    except StaleElementReferenceException:
        time.sleep(0.25)
        await select_option(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: could not change select value for '{}', message: '{}'".format(name, e))
        pass