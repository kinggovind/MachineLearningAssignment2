import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question 1. Numpy
gov = np.random.randint(1,20,15)
print(gov)
gov.resize(3,5)
print(gov)
print(gov.max(axis=1))
x = np.where(np.isin(gov,gov.max(axis=1)), 0, gov)
print(x)

# Question 2. Pandas

#1
df = pd.read_csv("data.csv")
#2
print(df.describe())
print(df.info())


print(df.isnull().values.any())
print(df.isnull().sum())

df['Calories'].fillna(value=df['Calories'].mean(), inplace=True)
print(df)
print(df.isnull().values.any())
dff = df[["Pulse","Calories"]].min()
df.groupby(["Duration","Pulse"]).agg(['min', 'max', 'count', 'mean'])
df[((df["Calories"]>500) & (df["Calories"]<1000))]
df[((df["Calories"]>500) | (df["Calories"]<100))]
df_modified = df.loc[:, df.columns != 'Maxpulse']
df_modified
df.drop(["Maxpulse"],axis=1,inplace=True)
df
df["Calories"] = df["Calories"].astype(int)
df.info()
df.plot.scatter(x="Duration",y="Calories")

##############################################

# 3. Matplotlib
# Data to plot
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()