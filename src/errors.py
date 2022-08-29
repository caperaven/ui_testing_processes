from src.actions.print_screen import print_screen, print_screen_sync
from src.data import state


async def set_error(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    results["summary"]["success"] = False
    results["summary"]["error_count"] = results["summary"]["error_count"] + 1
    await print_screen(driver, {"file": "${}.png".format(step_name)}, {})
    state["errors"].append(message)


def set_error_sync(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    results["summary"]["success"] = False
    results["summary"]["error_count"] = results["summary"]["error_count"] + 1
    print_screen_sync(driver, {"file": "${}.png".format(step_name)}, {})
    state["errors"].append(message)

