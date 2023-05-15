from src.wait.components import wait_for_crs


# Call this method to start the event monitor
async def crs_start_event_monitor(driver, results):
    print("************************* crs_start_event_monitor *************************")

    await wait_for_crs(driver, {"timeout": 30}, results)

    javascript = "return await globalThis.crs.call('debug', 'start_monitor_events', {})"
    driver.execute_script(javascript)

# Call this method to stop the event and log the result to the results object
async def crs_stop_event_monitor(driver, results):
    print("************************* crs_stop_event_monitor *************************")

    javascript = "return await globalThis.crs.call('debug', 'stop_monitor_events', {})"
    result = driver.execute_script(javascript)

    # add the result to the results object -- will need more logic to handle this
    if len(result) == 0:
        result = "no leaks detected"

    # add value to results object
    results["leaks"] = result
