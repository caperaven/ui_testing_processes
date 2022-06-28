from typing import Any
from src.elements import get_element


class SystemActions:
    @staticmethod
    async def attributes_to_variables(step, context, process, item):
        args = step["args"].copy()

        queries = args.keys()

        for query in queries:
            if query == "step": continue
            element = get_element(context.driver, {"query": query, "step": args["step"]}, context.current_result)
            if element is not None:
                element_def = args[query]
                attributes = element_def.keys()

                for attribute in attributes:
                    attr = element.get_attribute(attribute)
                    property = element_def[attribute]
                    context.set_value(property, attr, context, process, item)

    @staticmethod
    async def properties_to_variables(step, context, process, item):
        args = step["args"].copy()

        queries = args.keys()

        for query in queries:
            if query == "step": continue
            element = get_element(context.driver, {"query": query, "step": args["step"]}, context.current_result)
            if element is not None:
                element_def = args[query]
                properties = element_def.keys()

                for prop in properties:
                    attr = element.get_property(prop)
                    prop = element_def[prop]
                    context.set_value(prop, attr, context, process, item)

    @staticmethod
    async def audit(step, context, process, item):
        args = step["args"].copy()
        await context.scraper.run(context.driver, args, context.current_result)
        pass
