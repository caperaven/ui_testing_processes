from src.actions.navigate import navigate

class PerformActions:
    @staticmethod
    async def navigate(step, context, process, item):
        url = context.process.get_value(step["args"]["url"], context, process, item)
        results = {}
        await navigate(context.driver, {
            "url": url
        }, results)
        pass

    @staticmethod
    async def close_window(step, context, process, item):
        pass

    @staticmethod
    async def refresh(step, context, process, item):
        pass

    @staticmethod
    async def click(step, context, process, item):
        print("click")
        pass

    @staticmethod
    async def dbl_click(step, context, process, item):
        pass

    @staticmethod
    async def context_click(step, context, process, item):
        pass

    @staticmethod
    async def click_sequence(step, context, process, item):
        pass

    @staticmethod
    async def press_key(step, context, process, item):
        pass

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
        pass