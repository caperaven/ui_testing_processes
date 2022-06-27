from src.actions.print_screen import print_screen
import asyncio

async def set_error(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    results["summary"]["success"] = False
    results["summary"]["error_count"] = results["summary"]["error_count"] + 1
    await print_screen(driver, {"file": "${}.png".format(step_name)}, {})


def set_error_sync(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    results["summary"]["success"] = False
    results["summary"]["error_count"] = results["summary"]["error_count"] + 1
    asyncio.run(print_screen(driver, {"file": "${}.png".format(step_name)}, {}))
