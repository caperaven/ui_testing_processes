from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.errors import set_error_sync


def _get_query(args):
    if "id" in args:
        return "#{}".format(args["id"])
    else:
        return args["query"]


def _idle_condition():
    async def _predicate(driver):
        element = driver.find_element(By.CSS_SELECTOR, "body")
        value = element.get_attribute("idle")
        return value == "true"
    return _predicate


def wait_for_element(driver, context, query, results, step):
    wait = WebDriverWait(context, 240, poll_frequency=0.1)

    try:
        # wait for the element to be intractable
        result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, query)))
        # return the result
        return result
    except TimeoutException:
        set_error_sync(driver, results, step, "error: element '{}' not found".format(query))
        return None


def get_element(driver, args, results):
    query = _get_query(args)

    # the query is a path so find each element one at a time and return the end result
    if ' ' in query:
        return get_element_on_path(driver, args, results)

    # the query is a single element so wait for it to be intractable and return it
    return wait_for_element(driver, driver, query, results, args["step"])


def get_element_on_path(driver, args, results):
    query = _get_query(args)
    queries = query.split(" ")
    context = driver

    for query in queries:
        element = wait_for_element(driver, context, query, results, args["step"])

        if element is None:
            return None

        context = element

        # check if the element has a shadow root
        # if it does, we need to use that as the context for the next query
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)

        if shadow_root is not None:
            context = element.shadow_root

    # the last element is the result and since we are setting the context to the element
    # we can just return the context
    return context

