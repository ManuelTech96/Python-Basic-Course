import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Hard_file_problems\\categoria.csv")

sns.boxplot(x="categoria",y="valor",data = df)

plt.show()