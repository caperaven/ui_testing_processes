from src.errors import set_error


async def refresh(driver, args, results):
    try:
        driver.refresh()
        results[args["step"]] = "success"
    except Exception as e:
        print(e)
        await set_error(driver, results, args["step"], "error: refresh failed, '{}'".format(e))
        pass