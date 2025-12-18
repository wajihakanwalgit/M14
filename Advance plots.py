import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib as plt

df = pd.read_csv("iris dataaet.csv")

df.head()

plt.figure(figsize=(6,4))
sns.barplot(x="species", y="SepalLengthCm",data=df)
plt.title("Bar Plot: Species vs Sepal Length")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="species", data=df)
plt.title("Count Plot of Iris Species")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="species", y="SepalLengthCm", data=df)
plt.title("Box Plot: Species vs Sepal Width")
plt.show()

plt.figure(figsize=(6,4))
sns.swarmplot(x="species", y="SepalLengthCm", data=df)
plt.title("Swarm Plot: Species vs Sepal Width")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df["SepalWidthCm"], kde=True)
plt.title("Distribution of Sepal Width")
plt.show()

sns.jointplot(x="SepalWidthCm", y="SepalLengthCm", data=df,kind="scatter")
plt.show()

sns.pairplot(df,hue="Species")
plt.show()

