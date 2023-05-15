from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.data import data
from src.wait.components import wait_for_css_property, wait_for_attribute, wait_until_attribute
from src.errors import set_error
from src.memory import get_memory
import time
from src.crs_calls.crs_debug import crs_start_event_monitor, crs_stop_event_monitor
from src.action_systems.wait_actions import wait_for_crs


async def navigate(driver, args, results):
    try:
        driver.execute_script(data["scripts"]["idle-false"])
        url = args["url"]
        driver.get(url)
        nav_count = 0

       #Do check to see if the page is loaded before continuing
        await wait_for_crs(driver, {"timeout": 30}, results)

        #Check to see if string "#welcome" is in the url
        if "#welcome" in url and nav_count == 0:
            nav_count += 1
            print("Starting Monitor")
            print("url: ", url)
            await crs_start_event_monitor(driver, results)

        if "#welcome" in url and nav_count == 1:
            nav_count += 1
            print("Stopping Monitor")
            print("url: ", url)
            await crs_stop_event_monitor(driver, results)

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

        # await wait_for_attribute(driver, {
        #     "query": "view-container",
        #     "attr": "status",
        #     "value": "ready",
        #     "step": "navigate"
        # }, results)

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
