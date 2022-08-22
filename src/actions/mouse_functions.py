from selenium.webdriver.common.action_chains import ActionChains
from src.elements import get_element

async def drag_by(driver, args, results):
    args = args.copy()

    x = args["x"] if "x" in args else 0
    y = args["y"] if "y" in args else 0

    element = get_element(driver, args, results)
    action = ActionChains(driver)

    action.move_to_element(element).drag_and_drop_by_offset(element, x, y).perform()
    pass

async def hover_over_element(driver, args, results):
    pass