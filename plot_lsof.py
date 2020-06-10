import pandas as pd
import matplotlib.pyplot as plt


file = "lsof.log"
df = pd.read_json(file, lines=True)

df.plot(kind="line", x="time")
plt.xticks(rotation=15)
plt.show()
