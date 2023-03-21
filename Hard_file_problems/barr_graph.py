import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Hard_file_problems\\cofla_earnings.csv")

sns.barplot(x="fuente",y="ingresos",data = df)

#Geting total earnings
total_earnings = df['ingresos'].sum()

print(f"Total earnings are ${total_earnings} USD")

plt.show()