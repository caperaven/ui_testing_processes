from src.wait.components import wait_is_ready, wait_for_element, wait_for_attributes, wait_for_attribute, \
    wait_for_css_property, wait_for_property, wait_for_css_class, wait_for_children, wait_for_count, wait_for_time, \
    wait_for_selected, wait_for_windows, wait_until_idle, wait_for_text, wait_for_value, wait_until_attribute, \
    wait_until_attribute_gone


class WaitActions:
    @staticmethod
    async def time(step, context, process, item):
        args = step["args"].copy()
        await wait_for_time(context.driver, args, process["_results"])

    @staticmethod
    async def is_ready(step, context, process, item):
        args = step["args"].copy()
        await wait_is_ready(context.driver, args, process["_results"])

    @staticmethod
    async def element(step, context, process, item):
        args = step["args"].copy()
        await wait_for_element(context.driver, args, process["_results"])

    @staticmethod
    async def attribute(step, context, process, item):
        args = step["args"].copy()
        await wait_for_attribute(context.driver, args, process["_results"])

    @staticmethod
    async def attributes(step, context, process, item):
        args = step["args"].copy()
        await wait_for_attributes(context.driver, args, process["_results"])

    @staticmethod
    async def style_property(step, context, process, item):
        args = step["args"].copy()
        await wait_for_css_property(context.driver, args, process["_results"])

    @staticmethod
    async def element_property(step, context, process, item):
        args = step["args"].copy()
        await wait_for_property(context.driver, args, process["_results"])

    @staticmethod
    async def text_content(step, context, process, item):
        args = step["args"].copy()
        await wait_for_text(context.driver, args, process["_results"])

    @staticmethod
    async def text_value(step, context, process, item):
        args = step["args"].copy()
        await wait_for_value(context.driver, args, process["_results"])

    @staticmethod
    async def selected(step, context, process, item):
        args = step["args"].copy()
        await wait_for_selected(context.driver, args, process["_results"])

    @staticmethod
    async def child_count(step, context, process, item):
        args = step["args"].copy()
        await wait_for_children(context.driver, args, process["_results"])

    @staticmethod
    async def element_count(step, context, process, item):
        args = step["args"].copy()
        await wait_for_count(context.driver, args, process["_results"])

    @staticmethod
    async def window_count(step, context, process, item):
        args = step["args"].copy()
        await wait_for_windows(context.driver, args, process["_results"])

    @staticmethod
    async def idle(step, context, process, item):
        args = step["args"].copy()
        await wait_until_idle(context.driver, args, process["_results"])

    @staticmethod
    async def has_attribute(step, context, process, item):
        args = step["args"].copy()
        await wait_until_attribute(context.driver, args, process["_results"])
        pass

    @staticmethod
    async def has_not_attribute(step, context, process, item):
        args = step["args"].copy()
        await wait_until_attribute_gone(context.driver, args, process["_results"])
        pass

    @staticmethod
    async def has_class(step, context, process, item):
        args = step["args"].copy()
        await wait_for_css_class(context.driver, args, process["_results"])
        pass

    @staticmethod
    async def has_not_class(step, context, process, item):
        args = step["args"].copy()
        await _not_class_condition(context.driver, args, process["_results"])
        pass