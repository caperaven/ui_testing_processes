import time
from selenium.common.exceptions import StaleElementReferenceException
from src.elements import get_element
from src.errors import set_error
from src.utils import get_name
from src.memory import get_memory
from src.wait.components import wait_until_attribute_gone


async def type_text(driver, args, results):
    try:
        value = args["value"]
        element = get_element(driver, args, results)

        if element is None:
            return

        element.clear()
        element.send_keys(value)

        time.sleep(0.25)

        args["attr"] = "disabled"

        await wait_until_attribute_gone(driver, args, results)

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }
    except StaleElementReferenceException:
        time.sleep(0.25)
        await type_text(driver, args, results)
        pass
    except Exception as e:
        print(e)
        name = get_name(args)
        await set_error(driver, results, args["step"], "error: element '{}' not context clickable, '{}'".format(name, e))
        