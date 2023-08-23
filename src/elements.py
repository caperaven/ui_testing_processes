from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.errors import set_error_sync

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _get_query(args):
    if "id" in args:
        return "#{}".format(args["id"])
    else:
        return args["query"]


def _get_element(driver, args, results):
    query = _get_query(args)

    if ":shadow:" in query:
        parts = query.split(":")
        parent = driver.find_element(By.CSS_SELECTOR, parts[0])
        return parent.shadow_root.find_element(By.CSS_SELECTOR, parts[2])
    else:
        WebDriverWait(driver, 10).until(_element_condition(args, results))
        return driver.find_element(By.CSS_SELECTOR, query)


def _element_condition(args, results):
    def _predicate(driver):
        try:
            if "id" in args:
                locator = (By.ID, args["id"])
            elif "query" in args:
                locator = (By.CSS_SELECTOR, args["query"])
            else:
                raise ValueError("Either 'id' or 'query' should be provided in args.")

            element = driver.find_element(*locator)

            clickability_condition = EC.element_to_be_clickable(locator)
            condition = clickability_condition
            WebDriverWait(driver, 10).until(condition)
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
        return _get_element(driver, args, results)
    except Exception as e:
        print(e)
        set_error_sync(driver, results, args["step"], "error: element '{}' not found".format(query))
        return None
