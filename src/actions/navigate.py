from src.data import data
from src.wait.components import wait_for_css_property, wait_for_attribute
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

        await wait_for_css_property(driver, {
            "query": "body",
            "property": "visibility",
            "value": "hidden",
            "eval": "ne",
            "step": "navigate"
        }, results)

        driver.execute_script(data["scripts"]["idle-true"])

        await wait_for_attribute(driver, {
            "query": "body",
            "attr": "idle",
            "value": "true",
            "step": "navigate"
        }, results)

        await wait_for_attribute(driver, {
            "query": "view-container",
            "attr": "status",
            "value": "ready",
            "step": "navigate"
        }, results)

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
        time.sleep(2)

        args["url"] = open_url
        await navigate(driver, args, results)
        time.sleep(1)

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver, 1)
        }
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: could not open {} and close url '{}', '{}'".format(open_url, default_url, e))
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
