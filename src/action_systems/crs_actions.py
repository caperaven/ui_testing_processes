class CRSActions:
    @staticmethod
    async def call(step, context, process, item):
        driver = context.driver
        args = step["args"]
        results = process["_results"]
        print("I was called")
