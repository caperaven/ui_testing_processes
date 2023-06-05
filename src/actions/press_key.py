import time
from selenium.common.exceptions import StaleElementReferenceException
from src.elements import get_element
from src.errors import set_error
from src.utils import get_name
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.common.keys import Keys

async def press_key(driver, args, results):
    try:
        element = get_element(driver, args, results)

        if element is None:
            return

        key_values = args["key"].split("+")

        if len(key_values) > 1:
            action_chains = ActionChains(driver)

            for key_value in key_values:
                if key_value.upper() == "CONTROL":
                    action_chains.key_down(Keys.CONTROL)
                elif key_value.upper() == "SHIFT":
                    action_chains.key_down(Keys.SHIFT)
                elif key_value.upper() == "ALT":
                    action_chains.key_down(Keys.ALT)
                else:
                    action_chains.key_down(key_value)

            action_chains.perform()
        else:
            element.send_keys(key_values[0])

    except StaleElementReferenceException:
        time.sleep(0.25)
        await press_key(driver, args, results)
        pass

    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: could not press key '{}' on '{}', message: '{}'".format(args["key"], name, e))
        pass