from datetime import datetime
from src.data import state
import json
import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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

    save_chart(results)

    print("******* results saved *******")
    print(file)

def save_chart(results):
    #get the first item in the dictionary
    first_item = next(iter(results.items()))

    #get all the keys from the first item
    keys = first_item[1].keys()

    #loop through the keys
    for key in keys:
        if key == "summary":
            continue

        create_chart(first_item[1][key], os.path.join(state["folder"], key + ".png"))

def create_chart(results, path):
    del results['memory']

    data = results
    df = pd.DataFrame(data).transpose()
    df = df[['memory']]

    # Create the chart
    sns.lineplot(x=df.index, y='memory', data=df, linewidth=2)
    plt.xlabel('key')

    # Set the y-axis label to 'memory'
    max = df['memory'].max()
    plt.ylabel('memory')
    plt.ylim(0, max * 2)

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=25)

    plt.text(len(df) - 1, df['memory'].max(), str(df['memory'].max()))

    plt.savefig(path)

def create_chart_from_array(data, path):
    df = pd.DataFrame({"values": data})
    max = df["values"].max()
    plt.ylim(0, max * 2)
    sns.lineplot(data=df, linewidth=2)
    plt.savefig(path)

