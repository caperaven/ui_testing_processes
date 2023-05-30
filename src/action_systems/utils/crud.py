from datetime import datetime
from src.wait.components import wait_for_element, wait_for_attribute, wait_for_element_gone
from src.actions.click import click
from src.actions.type import type_text
from src.elements import _get_element

class ScreenType:
    CREATE = {
        "input": "#model_createResource_field-input",
        "button": "pragma-group[title='Create'] button",
        "dialog_query": "pragma-action-dialog dynamic-create"
    }
    EDIT = {
        "input": "#model_editResource_field-input",
        "button": "pragma-group[title='Edit'] button",
        "dialog_query": "pragma-action-dialog dynamic-update"
    }
    PREVIEW = {
        "input": "#model_previewResource_field-input",
        "button": "pragma-group[title='Preview'] button",
        "dialog_query": "pragma-action-dialog dynamic-peek"
    }
async def open_screen(driver, element_id, screen, results):
    try:
        await wait_for_element(driver, {
            "step": "wait for input",
            "query": element_id["input"]
        }, results)

        await type_text(driver, {
            "step": "type text",
            "query": element_id["input"],
            "value": screen
        }, results)

        await click(driver, {
            "step": "click button to open screen",
            "query": element_id["button"]
        }, results)

        await wait_for_attribute(driver, {
            "step": "wait for screen to open",
            "query": element_id["dialog_query"],
            "attr": "data-ready",
            "value": "true"
        }, results)

        return True
    except Exception as e:
        results["result"] = "error",
        results["error"] = str(e)
        print(e)
        return False
        pass


async def create_record(driver, screen, uuid, intents, results):
    await open_screen(driver, ScreenType.CREATE, screen, results)

    try:
        for intent in intents:
            tabs = intent["tabs"]
            element = intent["element"]
            value = parse_value(intent["value"], uuid)

            # click on the tabs in order to get to the input
            for tab_query in tabs:
                await click(driver, {
                    "step": "click on tab",
                    "query": tab_query
                }, results)

            try:
                # see if the element exists and if it does not continue
                _get_element(driver, element)
            except Exception as e:
                continue
                pass

            # type the value into the input
            await type_text(driver, {
                "step": "type text",
                "query": element,
                "value": value
            }, results)

        await click(driver, {
            "step": "click on save button",
            "query": "pragma-action-dialog pragma-action-button.primary"
        }, results)

        await wait_for_element_gone(driver, {
            "step": "wait for screen to close",
            "query": "pragma-action-dialog"
        }, results)
    except Exception as e:
        results["result"] = "error",
        results["error"] = str(e)
        print(e)
        return False
        pass
def parse_value(value, uuid):
    # 1. value is not a string so return the value
    if not isinstance(value, str):
        return value

    # 2. check if it contains $uuid and if it does, replace it with the uuid
    if "$uuid" in value:
        value = value.replace("$uuid", uuid)

    # 3. check if it contains $now and if it does, replace it with the current datetime
    if value == "$now":
        return datetime.now()

    return value

async def edit_record(driver, screen, uuid, results):
    pass

async def preview_record(driver, screen, uuid, results):
    pass