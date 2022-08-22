from src.actions.navigate import navigate, close_window
from src.actions.refresh import refresh
from src.actions.click import click, dbl_click, context_click, click_sequence
from src.actions.press_key import press_key
from src.actions.type import type_text
from src.actions.print_screen import print_screen
from src.actions.select_option import select_option
from src.actions.switch_to import switch_to_default, switch_to_frame, switch_to_tab
from src.actions.mouse_functions import drag_by, hover_over_element, mouse_drag
from src.utils import update_args_value

class PerformActions:
    @staticmethod
    async def navigate(step, context, process, item):
        await navigate(context.driver, step["args"], context.current_result)

    @staticmethod
    async def close_window(step, context, process, item):
        await close_window(context.driver, step["args"], context.current_result)

    @staticmethod
    async def refresh(step, context, process, item):
        await refresh(context.dirver, step["args"], context.current_result)

    @staticmethod
    async def click(step, context, process, item):
        await click(context.driver, step["args"], context.current_result)

    @staticmethod
    async def dbl_click(step, context, process, item):
        await dbl_click(context.driver, step["args"], context.current_result)

    @staticmethod
    async def context_click(step, context, process, item):
        await context_click(context.driver, step["args"], context.current_result)

    @staticmethod
    async def click_sequence(step, context, process, item):
        await click_sequence(context.driver, step["args"], context.current_result)

    @staticmethod
    async def press_key(step, context, process, item):
        await press_key(context.driver, step["args"], context.current_result)

    @staticmethod
    async def print_screen(step, context, process, item):
        await print_screen(context.driver, step["args"], context.current_result)

    @staticmethod
    async def select_option(step, context, process, item):
        await select_option(context.driver, step["args"], context.current_result)

    @staticmethod
    async def switch_to_frame(step, context, process, item):
        await switch_to_frame(context.driver, step["args"], context.current_result)

    @staticmethod
    async def switch_to_default(step, context, process, item):
        await switch_to_default(context.driver, step["args"], context.current_result)

    @staticmethod
    async def switch_to_tab(step, context, process, item):
        await switch_to_tab(context.driver, step["args"], context.current_result)

    @staticmethod
    async def type_text(step, context, process, item):
        update_args_value(step, context, process, item, "value")
        await type_text(context.driver, step["args"], context.current_result)

    @staticmethod
    async def drag_by(step, context, process, item):
        await drag_by(context.driver, step["args"], context.current_result)

    @staticmethod
    async def hover_over_element(step, context, process, item):
        await hover_over_element(context.driver, step["args"], context.current_result)

    @staticmethod
    async def mouse_drag(step, context, process, item):
        await mouse_drag(context.driver, step["args"], context.current_result)