from src.actions.print_screen import print_screen, print_screen_sync
from src.data import state


async def set_error(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    await print_screen(driver, {"file": "${}.png".format(step_name)}, {})
    state["errors"].append(message)


def set_error_sync(driver, results, step_name, message):
    print(message)
    results[step_name] = message
    print_screen_sync(driver, {"file": "${}.png".format(step_name)}, {})
    state["errors"].append(message)

