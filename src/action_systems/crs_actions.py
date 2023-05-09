class CRSActions:
    @staticmethod
    async def call(step, context, process, item):
        driver = context.driver
        args = step["args"]

        type = args["type"]
        action = args["action"]
        args = args["args"]

        # javascript = f"return crs.call(arguments[0], arguments[1], arguments[2])"
        # result = driver.execute_async_script(javascript, type, action, args)

        return "hello world"

