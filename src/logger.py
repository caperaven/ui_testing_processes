from src.data import state


class Logger:
    @staticmethod
    def test_started(name):
        state["errors"] = []
        name = Logger.sanitize(name)
        print("##teamcity[testStarted name='{}']".format(name))

    @staticmethod
    def test_finished(name):
        if len(state["errors"]) > 0:
            name = Logger.sanitize(name)
            error_text = Logger.sanitize(state["errors"][0])
            print("##teamcity[testFailed name='{}' message='{}']".format(name, error_text))

        print("##teamcity[testFinished name='{}']".format(Logger.sanitize(name)))

    @staticmethod
    def sanitize(txt):
        for c in "|'\\[]":
            txt = txt.replace(c, "|{}".format(c))
        return txt
