from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from src.elements import get_element


async def drag_by(driver, args, results):
    args = args.copy()

    x = args["x"] if "x" in args else 0
    y = args["y"] if "y" in args else 0

    element = await get_element(driver, args, results)
    action = ActionChains(driver)
    action.move_to_element(element).drag_and_drop_by_offset(element, x, y).perform()
    pass


async def hover_over_element(driver, args, results):
    element = await get_element(driver, args, results)
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    pass


async def mouse_drag(driver, args, results):
    args = args.copy()

    element = await get_element(driver, args, results)
    location = element.location

    start = args["start_at"]
    start_x = start["x"] + location["x"]
    start_y = start["y"] + location["y"]

    to = args["move_too"]
    to_x = to["x"] + location["x"]
    to_y = to["y"] + location["y"]

    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(start_x, start_y)
    action.pointer_action.pointer_down(MouseButton.LEFT)
    action.pointer_action.move_to_location(to_x, to_y)
    action.pointer_action.pointer_up()
    action.perform()
    action.clear_actions()
    pass
