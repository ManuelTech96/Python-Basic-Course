import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Hard_file_problems\\fart.csv")

sns.lineplot(x="fecha",y="pedos",data = df)

#Creating a point at the day with more farts
plt.plot("01-09", 17, "o")

plt.show()