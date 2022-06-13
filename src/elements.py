from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.errors import set_error
import asyncio


def _get_query(args):
    if "id" in args:
        return "#{}".format(args["id"])
    else:
        return args["query"]


def _get_element(driver, query):
    if ":shadow:" in query:
        parts = query.split(":")
        parent = driver.find_element(By.CSS_SELECTOR, parts[0])
        return parent.shadow_root.find_element(By.CSS_SELECTOR, parts[2])
    else:
        WebDriverWait(driver, 10).until(_element_condition(query))
        return driver.find_element(By.CSS_SELECTOR, query)


def _element_condition(query):
    def _predicate(driver):
        try:
            element = driver.find_element(By.CSS_SELECTOR, query)
            return False if element is None else True
        except Exception as e:
            return False
    return _predicate


def _idle_condition():
    async def _predicate(driver):
        element = driver.find_element(By.CSS_SELECTOR, "body")
        value = element.get_attribute("idle")
        return value == "true"
    return _predicate


def get_element(driver, args, results):
    query = _get_query(args)

    try:
        return _get_element(driver, query)
    except Exception as e:
        print(e)
        asyncio.run(set_error(driver, results, args["step"], "error: element '{}' not found".format(query)))
        return None
        pass
