from datetime import datetime
from src.data import state
import json
import os


def set_results_folder(folder):
    now = datetime.now()
    date_folder = "test_results_{}_{}_{}_{}_{}_{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    path = os.path.join(folder, date_folder)
    state["folder"] = path

    if not os.path.exists(path):
        os.makedirs(path)


def save_results(results):
    path = state["folder"]

    file = os.path.realpath(os.path.join(path, "_result.json"))

    outfile = open(file, "w")
    json.dump(results, outfile, indent=4)
    outfile.close()

    print("******* results saved *******")
    print(file)
