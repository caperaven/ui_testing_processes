from src.elements import get_element
import time
import os
import uuid

class SystemActions:
    @staticmethod
    async def attributes_to_variables(step, context, process, item):
        args = step["args"].copy()

        queries = args.keys()

        for query in queries:
            if query == "step": continue
            element = get_element(context.driver, {"query": query, "step": args["step"]}, process["_results"])
            if element is not None:
                element_def = args[query]
                attributes = element_def.keys()

                for attribute in attributes:
                    attr = element.get_attribute(attribute)
                    property = element_def[attribute]
                    context.set_value(property, attr, context, process, item)

        process["_results"][args["step"]] = "success"

    @staticmethod
    async def properties_to_variables(step, context, process, item):
        args = step["args"].copy()

        queries = args.keys()

        for query in queries:
            if query == "step": continue
            element = get_element(context.driver, {"query": query, "step": args["step"]}, process["_results"])
            if element is not None:
                element_def = args[query]
                properties = element_def.keys()

                for prop in properties:
                    attr = element.get_property(prop)
                    prop = element_def[prop]
                    context.set_value(prop, attr, context, process, item)

        process["_results"][args["step"]] = "success"

    @staticmethod
    async def dimensions_to_variables(step, context, process, item):
        args = step["args"].copy()

        queries = args.keys()

        for query in queries:
            if query == "step": continue
            element = get_element(context.driver, {"query": query, "step": args["step"]}, process["_results"])
            if element is not None:
                location = element.location
                size = element.size
                prop = args[query]["variable"]
                obj = {
                    "x": location["x"],
                    "y": location["y"],
                    "width": size["width"],
                    "height": size["height"]
                }
                context.set_value(prop, obj, context, process, item)

        process["_results"][args["step"]] = "success"

    @staticmethod
    async def set_variables(step, context, process, item):
        args = step["args"].copy()
        variables = args.keys()

        for variable in variables:
            if variable == "step": continue
            value = args[variable]
            context.set_value(variable, value, context, process, item)

        process["_results"][args["step"]] = "success"

    @staticmethod
    async def set_uuid_variables(step, context, process, item):
        args = step["args"].copy()
        variables = args["variables"]

        for variable in variables:
            value = uuid.uuid4()
            context.set_value(variable, value, context, process, item)

        process["_results"][args["step"]] = "success"

    @staticmethod
    async def audit(step, context, process, item):
        args = step["args"].copy()
        await context.scraper.run(context.driver, args, process["_results"])
        pass

    @staticmethod
    async def add_to_variables(step, context, process, item):
        args = step["args"].copy()
        variables = args.keys()

        for variable in variables:
            if variable == "step": continue
            value = context.get_value(variable, context, process, item)
            add_value = args[variable]
            result = value + add_value
            context.set_value(variable, result, context, process, item)

        process["_results"][args["step"]] = "success"
        pass

    @staticmethod
    async def sleep(step, context, process, item):
        args = step["args"].copy()
        duration = args["duration"]
        time.sleep(duration)
        process["_results"][args["step"]] = "success"

    @staticmethod
    async def process(step, context, process, item):
        current_step = process["current_step"]
        args = step["args"].copy()
        results = process["_results"][current_step] = {}

        child_process = await context.run_process(args, context, process, item)

        keys = child_process["_results"].keys()
        for key in keys:
            results[key] = child_process["_results"][key]

    @staticmethod
    async def template(step, context, process, item):
        current_step = process["current_step"]
        args = step["args"].copy()
        results = process["_results"][current_step] = {}

        schema_name = args["schema"]
        process_name = args["process"]

        template_schema = context.process_schema_registry.get_template(schema_name)
        template_process = template_schema[process_name].copy()

        current_schema = context.current["schema"]
        context.current["schema"] = template_schema

        child_process = await context.run_process(args, context, process, item)

        context.current["schema"] = current_schema

        keys = child_process["_results"].keys()
        for key in keys:
            results[key] = child_process["_results"][key]

    @staticmethod
    async def run_script(step, context, process, item):
        args = step["args"].copy()
        script_file = args["script"]
        path_parts = os.path.split(context.current["schema"]["file_path"])
        script_path = os.path.join(path_parts[0], script_file);

        file = open(script_path)
        content = file.read()
        context.driver.execute_script(content)





