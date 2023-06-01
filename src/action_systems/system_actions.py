from selenium.common import StaleElementReferenceException

from src.action_systems.utils.get_crud_screens import get_crud_screens
from src.action_systems.utils.check_crud_screen_dictionary import get_intent
from src.actions.navigate import open_and_close_url
from src.actions.click import click
from src.data import state
from src.elements import get_element
from src.action_systems.utils.crud import create_record, edit_record, preview_record
import time
import os
import uuid

from src.errors import set_error
from src.memory import get_memory
from src.results_writer import create_chart_from_array, save_json_to_file
from src.wait.components import wait_for_attribute, wait_for_element


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
            context.set_value(variable, str(value), context, process, item)

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
        script_path = os.path.join(path_parts[0], script_file)

        file = open(script_path)
        content = file.read()
        context.driver.execute_script(content)

    @staticmethod
    async def show_all_screens(step, context, process, item):
        context.driver.execute_script("console.clear()")

        menu_items = context.driver.execute_script("return document.querySelector('pr-menu')._flatList")
        memory = []
        log = []
        logId = 0

        mem = get_memory(context.driver, 1)
        memory.append(mem)

        add_to_log(context, log, memory, logId, "start_test")

        subset = menu_items         #menu_items[:5]

        for item in subset:
            if "screen" in item and item["screen"] != "" and item["screen"] is not None:
                logId += 1
                await open_and_close_url(context.driver, {
                    "open_url": "".join([state["server"], item["screen"]]),
                    "default_url": "".join([state["server"], "#welcome"]),
                    "step": step["args"]["step"]
                }, process["_results"])

                add_to_log(context, log, memory, logId, item["screen"])

        add_to_log(context, log, memory, logId + 1, "end_text")

        create_chart_from_array(memory, os.path.join(state["folder"], "all_dashboards_memory.png"))
        save_json_to_file(log, os.path.join(state["folder"], "all_dashboards_memory.json"))

    @staticmethod
    async def open_side_menu(step, context, process, item):
        args = step["args"].copy()

        # what is the button on the side menu to click
        menu = args["menu"]

        # once you have clicked on the button, what element should you wait for
        wait_for = args["wait_for"]

        results = process["_results"]
        driver = context.driver

        try:
            button = get_element(driver, {
                "step": "open_side_menu",
                "query": "pr-side-menu #{}".format(menu),
                "timeout": 360
            }, results)

            is_open = button.get_attribute("data-expanded") == "true"

            if not is_open:
                await click(driver, {
                    "step": "open_side_menu",
                    "query": "pr-side-menu #{}".format(menu),
                }, results)

                await wait_for_element(driver, {
                    "step": "wait_for",
                    "query": wait_for
                }, results)

            results[args["step"]] = {
                "result": "success",
                "memory": get_memory(driver)
            }
        except Exception as e:
            print(e)
            await set_error(driver, results, args["step"], "Open Side Menu - {} had error - {}".format(menu, e))
            pass

    @staticmethod
    async def check_crud_screens(step, context, process, item):
        args = step["args"].copy()
        results = process["_results"]
        driver = context.driver

        screens = get_crud_screens()

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver),
            "screens": []
        }

        result = results[args["step"]]

        try:
            for screen in screens:
                driver.execute_script("console.clear()")
                create_intents = get_intent(screen)
                uuid_value = str(uuid.uuid4())

                screenResult = {
                    "screen": screen,
                    "action": "create",
                    "result": "success",
                }

                try:
                    await create_record(driver, screen, uuid_value, create_intents, screenResult)
                    await edit_record(driver, screen, uuid_value, screenResult)
                    await preview_record(driver, screen, uuid_value, screenResult)
                except Exception as e:
                    screenResult["result"] = "error"
                    screenResult["error"] = str(e)
                    print(e)
                    pass

                result["memory"] = get_memory(driver)
                result["screens"].append(screenResult)
        except Exception as e:
            result["result"] = "error"
            result["error"] = e
            pass

def add_to_log(context, log, memory, id, screen):
    mem = get_memory(context.driver, 0.5)

    logItem = {
        "id": id,
        "screen": screen,
        "memory": mem
    }

    log_entries = context.driver.get_log("browser")
    if (log_entries is not None and len(log_entries) > 0):
        logItem["console"] = log_entries

    context.driver.execute_script("console.clear()")

    log.append(logItem)
    memory.append(mem)