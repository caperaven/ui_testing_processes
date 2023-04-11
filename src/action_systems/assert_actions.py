from src.assertions.assert_attribute import assert_attributes, assert_attr_eq, assert_attr_neq, assert_has_attr, assert_has_not_attr, assert_has_class, assert_has_not_class
from src.assertions.assert_child_count import assert_child_count_eq, assert_child_count_neq
from src.assertions.assert_css import assert_style_eq, assert_style_neq
from src.assertions.assert_property import assert_property_eq, assert_property_neq
from src.assertions.assert_tag_name import assert_tag_name_eq, assert_tag_name_neq
from src.assertions.assert_text import assert_text_eq, assert_text_neq
from src.assertions.assert_value import assert_value_eq, assert_value_neq
from src.utils import update_args_value
from src.errors import set_error
from src.elements import get_element
from selenium.webdriver.common.by import By
from src.elements import _get_query

class AssertActions:
    @staticmethod
    async def attributes(step, context, process, item):
        await assert_attributes(context.driver, step["args"], process["_results"])

    @staticmethod
    async def attribute_eq(step, context, process, item):
        await assert_attr_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def attribute_neq(step, context, process, item):
        await assert_attr_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def has_attribute(step, context, process, item):
        await assert_has_attr(context.driver, step["args"], process["_results"])

    @staticmethod
    async def has_not_attribute(step, context, process, item):
        await assert_has_not_attr(context.driver, step["args"], process["_results"])

    @staticmethod
    async def child_count_eq(step, context, process, item):
        await assert_child_count_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def child_count_neq(step, context, process, item):
        await assert_child_count_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def style_property_eq(step, context, process, item):
        await assert_style_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def style_property_neq(step, context, process, item):
        await assert_style_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def element_property_eq(step, context, process, item):
        update_args_value(step, context, process, item, "value")
        await assert_property_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def element_property_neq(step, context, process, item):
        await assert_property_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def tag_name_eq(step, context, process, item):
        await assert_tag_name_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def tag_name_neq(step, context, process, item):
        await assert_tag_name_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def text_content_eq(step, context, process, item):
        await assert_text_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def text_content_neq(step, context, process, item):
        await assert_text_neq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def value_eq(step, context, process, item):
        await assert_value_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def value_neq(step, context, process, item):
        await assert_value_eq(context.driver, step["args"], process["_results"])

    @staticmethod
    async def variables_eq(step, context, process, item):
        args = step["args"].copy()
        variables = args.keys()

        errors = []

        for variable in variables:
            if variable == "step": continue

            expected = context.get_value(args[variable], context, process, item)
            value = context.get_value(variable, context, process, item)

            if value != expected:
                errors.append("error: value '{}' was ({}) should be ({})".format(variable, value, expected))

        if len(errors) > 0:
            await set_error(context.driver, process["_results"], args["step"], errors)
        else:
            process["_results"][args["step"]] = "success"
        pass

    @staticmethod
    async def variables_neq(step, context, process, item):
        args = step["args"].copy()
        variables = args.keys()

        errors = []

        for variable in variables:
            if variable == "step": continue

            expected = context.get_value(args[variable], context, process, item)
            value = context.get_value(variable, context, process, item)

            if value == expected:
                errors.append("error: value '{}' was ({}) should not be ({})".format(variable, value, expected))

        if len(errors) > 0:
            await set_error(context.driver, process["_results"], args["step"], errors)
        else:
            process["_results"][args["step"]] = "success"
        pass

    @staticmethod
    async def has_class(step, context, process, item):
        args = step["args"].copy()
        element = get_element(context.driver, args, process["_results"])
        cls = element.get_attribute("class")
        sub = args["class"]
        if sub in cls:
            process["_results"][args["step"]] = "success"
        else:
            await set_error(context.driver, process["_results"], args["step"], "class '{}' expected on '{}".format(sub, args["query"]));
        pass;

    @staticmethod
    async def has_not_class(step, context, process, item):
        args = step["args"].copy()
        element = get_element(context.driver, args, process["_results"])
        cls = element.get_attribute("class")
        sub = args["class"]
        if sub not in cls:
            process["_results"][args["step"]] = "success"
        else:
            await set_error(context.driver, process["_results"], args["step"], "class '{}' should not be on '{}".format(sub, args["query"]));
        pass;

    @staticmethod
    async def element_exists(step, context, process, item):
        args = step["args"].copy()
        query = _get_query(args)
        element = context.driver.find_element(By.CSS_SELECTOR, query)
        if element is not None:
            process["_results"][args["step"]] = "success"
        else:
            await set_error(context.driver, process["_results"], args["step"], "element '{}' should exist".format(args["query"]));
        pass

    @staticmethod
    async def element_not_exists(step, context, process, item):
        args = step["args"].copy()
        query = _get_query(args)

        success = False
        try:
            element = context.driver.find_element(By.CSS_SELECTOR, query)
        except Exception as e:
            success = True

        if success:
            process["_results"][args["step"]] = "success"
        else:
            await set_error(context.driver, process["_results"], args["step"], "element '{}' should NOT exist".format(args["query"]));
        pass
