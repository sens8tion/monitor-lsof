import pandas as pd
import matplotlib.pyplot as plt

import requests

url = "http://192.168.1.105:5000/NumLSOF"
dftab = pd.DataFrame()

fig, ax = plt.subplots()
plt.xticks(rotation=15)
plt.ylabel("open files")
fig.suptitle(url)
first = True
colour = {"homeassistant": "red", "root": "blue", "all": "green"}

while True:
    r = requests.get(url)
    jsonRow = r.json()
    dfr = pd.DataFrame.from_dict(jsonRow["lsof"], orient="index")
    dftab = dftab.append(dfr.T)

    for col in dftab.columns:
        if col != "time":
            plt.plot(dftab["time"], dftab[col], label=col, color=colour[col])

    if first:
        first = False
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(labels)

    frequency = int(len(dftab.index) / 8) + 1
    plt.xticks(dftab["time"][::frequency])

    plt.draw()
    plt.pause(1)
