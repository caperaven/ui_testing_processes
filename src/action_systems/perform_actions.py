from src.actions.navigate import navigate, close_window
from src.actions.refresh import refresh
from src.actions.click import click, dbl_click, context_click, click_sequence
from src.actions.press_key import press_key
from src.actions.type import type_text


class PerformActions:
    @staticmethod
    async def navigate(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await navigate(context.driver, args, results)

    @staticmethod
    async def close_window(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await close_window(context.driver, args, results)

    @staticmethod
    async def refresh(step, context, process, item):
        results = {}
        await refresh(context.dirver, {"step": context.current_step}, results)

    @staticmethod
    async def click(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await click(context.driver, args, results)

    @staticmethod
    async def dbl_click(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await dbl_click(context.driver, args, results)

    @staticmethod
    async def context_click(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await context_click(context.driver, args, results)

    @staticmethod
    async def click_sequence(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await click_sequence(context.driver, args, results)

    @staticmethod
    async def press_key(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await press_key(context.driver, args, results)

    @staticmethod
    async def print_screen(step, context, process, item):
        pass

    @staticmethod
    async def select_option(step, context, process, item):
        pass

    @staticmethod
    async def switch_to_frame(step, context, process, item):
        pass

    @staticmethod
    async def switch_to_default(step, context, process, item):
        pass

    @staticmethod
    async def switch_to_tab(step, context, process, item):
        pass

    @staticmethod
    async def type_text(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step
        results = {}
        await type_text(context.driver, args, results)
