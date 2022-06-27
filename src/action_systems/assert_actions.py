from src.assertions.assert_attribute import assert_attributes, assert_attr_eq, assert_attr_neq
from src.assertions.assert_child_count import assert_child_count_eq, assert_child_count_neq
from src.assertions.assert_css import assert_style_eq, assert_style_neq
from src.assertions.assert_property import assert_property_eq, assert_property_neq
from src.assertions.assert_tag_name import assert_tag_name_eq, assert_tag_name_neq
from src.assertions.assert_text import assert_text_eq, assert_text_neq
from src.assertions.assert_value import assert_value_eq, assert_value_neq


class AssertActions:
    @staticmethod
    async def attributes(step, context, process, item):
        args = step["args"].copy()
        await assert_attributes(context.driver, args, context.current_result)

    @staticmethod
    async def attribute_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_attr_eq(context.driver, args, context.current_result)

    @staticmethod
    async def attribute_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_attr_neq(context.driver, args, context.current_result)

    @staticmethod
    async def child_count_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_child_count_eq(context.driver, args, context.current_result)

    @staticmethod
    async def child_count_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_child_count_neq(context.driver, args, context.current_result)

    @staticmethod
    async def style_property_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_style_eq(context.driver, args, context.current_result)

    @staticmethod
    async def style_property_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_style_neq(context.driver, args, context.current_result)

    @staticmethod
    async def element_property_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_property_eq(context.driver, args, context.current_result)

    @staticmethod
    async def element_property_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_property_neq(context.driver, args, context.current_result)

    @staticmethod
    async def tag_name_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_tag_name_eq(context.driver, args, context.current_result)

    @staticmethod
    async def tag_name_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_tag_name_neq(context.driver, args, context.current_result)

    @staticmethod
    async def text_content_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_text_eq(context.driver, args, context.current_result)

    @staticmethod
    async def text_content_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_text_neq(context.driver, args, context.current_result)

    @staticmethod
    async def value_eq(step, context, process, item):
        args = step["args"].copy()
        await assert_value_eq(context.driver, args, context.current_result)

    @staticmethod
    async def value_neq(step, context, process, item):
        args = step["args"].copy()
        await assert_value_eq(context.driver, args, context.current_result)