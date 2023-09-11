from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


async def get(driver, args):
    query = args.get("element")
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    element = await get_element(context, query, timeout)

    if "attribute" in args:
        return element.get_attribute(args["attribute"])

    if "property" in args:
        return element.get_property(args["property"])

    return element


async def get_element(driver, query, timeout):
    if isinstance(query, WebElement):
        return query

    if ' ' in query:
        return await get_element_on_path(driver, query, timeout)
    else:
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, query)))
        return element


async def get_element_on_path(driver, query, timeout):
    queries = query.split(" ")
    context = driver

    for query in queries:
        use_shadow_root = query.endswith("::host")

        if use_shadow_root:
            query = query[:-6]

        element = await get_element(context, query, timeout)

        if element is None:
            return None

        context = element

        if use_shadow_root:
            shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)

            if shadow_root is not None:
                context = element.shadow_root

    return context
