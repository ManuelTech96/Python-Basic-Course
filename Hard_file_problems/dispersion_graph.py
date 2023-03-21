import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Hard_file_problems\\dispersion.csv")

sns.scatterplot(x="tiempo",y="dinero",data = df)

plt.show()