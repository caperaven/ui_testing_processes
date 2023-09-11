import time
from selenium.webdriver import Keys, ActionChains
from src.selenium.get import get_element
from src.selenium.wait import wait


async def perform(driver, args):
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    query = args.get("element")
    element = await get_element(context, query, timeout)
    action = args["action"]
    chain = ActionChains(driver)
    count = args.get("count", 1)

    args["driver"] = driver

    await Actions.scroll_into_view(element, chain, args)

    for i in range(count):
        await Actions.__dict__[action](element, chain, args)
        time.sleep(0.1)

    del args["driver"]

    if "wait" in args:
        await wait(driver, {
            "query": args["wait"]
        })


class Actions:
    @staticmethod
    async def click(element, chain, args=None):
        element.click()

    @staticmethod
    async def double_click(element, chain, args=None):
        element.double_click()

    @staticmethod
    async def context_click(element, chain, args=None):
        element.context_click()

    @staticmethod
    async def clear(element, chain, args=None):
        element.clear()

    @staticmethod
    async def type(element, chain, args):
        text = args["text"]

        element.clear()
        time.sleep(0.1)
        element.send_keys(text)
        time.sleep(0.25)
        element.send_keys(Keys.ENTER)

    @staticmethod
    async def hover(element, chain, args=None):
        chain.move_to_element(element).perform()

    @staticmethod
    async def key_down(element, chain, args=None):
        key = args["key"]
        chain.key_down(key).perform()

    @staticmethod
    async def key_up(element, chain, args=None):
        key = args["key"]
        chain.key_up(key).perform()

    @staticmethod
    async def scroll_into_view(element, chain, args):
        driver = args["driver"]
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    async def move_to(element, chain, args):
        # get current position
        current_x = element.location["x"]
        current_y = element.location["y"]

        # get target position
        x = args["x"]
        y = args["y"]

        # calculate offset
        offset_x = x - current_x
        offset_y = y - current_y

        # move to target
        chain.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()

    @staticmethod
    async def move_by(element, chain, args):
        x = args["x"]
        y = args["y"]
        chain.drag_and_drop_by_offset(element, x, y).perform()

    @staticmethod
    async def drag_and_drop(element, chain, args):
        target = args["target"]
        element.drag_and_drop(target)

    @staticmethod
    async def drag_and_drop_by(element, chain, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by(x, y)

    @staticmethod
    async def drag_and_drop_by_offset(element, chain, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by_offset(x, y)

    @staticmethod
    async def send_keys(element, chain, args):
        keys = args["keys"]
        element.send_keys(keys)
