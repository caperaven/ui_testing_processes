from src.errors import set_error
from src.memory import get_memory


async def refresh(driver, args, results):
    try:
        driver.refresh()

        results[args["step"]] = {
            "result": "success",
            "memory": get_memory(driver)
        }
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: refresh failed, '{}'".format(e))