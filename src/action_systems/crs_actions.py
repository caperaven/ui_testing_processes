class CRSActions:
    @staticmethod
    async def call(step, context, process, item):
        driver = context.driver
        args = step["args"]

        type = args["type"]
        action = args["action"]
        args = args["args"]

        javascript = "return await crs.call('{}', '{}', arguments[0])".format(type, action)
        result = driver.execute_script(javascript, args)

        return result

