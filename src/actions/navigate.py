from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.data import data
from src.wait.components import wait_until_attribute
from src.errors import set_error
from src.memory import get_memory
import time


async def navigate(driver, args, results):
    try:
        driver.execute_script(data["scripts"]["idle-false"])
        url = args["url"]
        driver.get(url)

        if "refresh" in args and args["refresh"] is True:
            driver.refresh()

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver, 1)
        }
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: could not navigate to '{}', '{}'".format(url, e))
        pass


async def open_and_close_url(driver, args, results):
    try:
        open_url = args["open_url"]
        default_url = args["default_url"]

        args["url"] = open_url
        await navigate(driver, args, results)
        time.sleep(1)
        await open_edit(driver, args, results)
        time.sleep(1)
        args["url"] = open_url
        await navigate(driver, args, results)
        time.sleep(1)

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver, 1)
        }
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"],
                        "error: could not open {} and close url '{}', '{}'".format(open_url, default_url, e))
        pass


async def close_window(driver, args, results):
    try:
        index = args["index"]

        if index == "last":
            index = len(driver.window_handles) - 1

        driver.switch_to.window(driver.window_handles[index])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: could not close window at ({}), '{}'".format(index, e))
        pass


async def open_edit(driver, args, results):
    element = None
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".grid-row")
    except:
        return

    if element is not None:
        action = ActionChains(driver).double_click(element)
        action.perform()
        time.sleep(1)

        await wait_until_attribute(driver, {
            "step": "open_edit",
            "query": "dynamic-update",
            "attr": "status",
            "value": "ready",
            "timeout": 10
        }, results)

        close_element = driver.find_element(By.CSS_SELECTOR, "pragma-action-dialog #close")
        close_element.click()
        time.sleep(1)
