from src.wait.components import wait_is_ready, wait_for_element, wait_for_attributes, wait_for_attribute, \
    wait_for_css_property, wait_for_property, wait_for_css_class, wait_for_children, wait_for_count, wait_for_time, \
    wait_for_selected, wait_for_windows, wait_until_idle, wait_for_text, wait_for_value


class WaitActions:
    @staticmethod
    async def time(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_time(context.driver, args, results)

    @staticmethod
    async def is_ready(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_is_ready(context.driver, args, results)

    @staticmethod
    async def element(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_element(context.driver, args, results)

    @staticmethod
    async def attribute(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_attribute(context.driver, args, results)

    @staticmethod
    async def attributes(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_attributes(context.driver, args, results)

    @staticmethod
    async def style_property(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_css_property(context.driver, args, results)

    @staticmethod
    async def element_properties(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_property(context.driver, args, results)

    @staticmethod
    async def text_content(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_text(context.driver, args, results)

    @staticmethod
    async def text_value(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_value(context.driver, args, results)

    @staticmethod
    async def selected(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_selected(context.driver, args, results)

    @staticmethod
    async def child_count(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_children(context.driver, args, results)

    @staticmethod
    async def element_count(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_count(context.driver, args, results)

    @staticmethod
    async def window_count(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_windows(context.driver, args, results)

    @staticmethod
    async def idle(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_until_idle(context.driver, args, results)

    @staticmethod
    async def has_attribute(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_css_property(context.driver, args, results)
        pass

    @staticmethod
    async def has_not_attribute(step, context, process, item):
        args = step["args"]
        args["step"] = context.current_step

        results = {}
        await wait_for_css_property(context.driver, args, results)
        pass