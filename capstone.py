import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("penguins")
df.head(10)
df.tail()
df.shape
df.dtypes
df.info()
df.isnull().sum()
df.describe()
df.describe().T
df.describe(include='all')
corr = df.corr(numeric_only=True)
sns.heatmap(corr, cmap='Wistia', annot=True)
plt.show()
df.hist(figsize=(12,8))
plt.show()
df.plot(
    kind="box",
    subplots=True,
    layout=(3,2),
    sharex=False,
    sharey=False,
    figsize=(8,12)
)
plt.show()
df.island.value_counts()
df.species.value_counts()
sns.countplot(data=df, x='sex', palette='summer')
plt.show()
sns.countplot(data=df, x='island', palette='RdPu')
plt.show()
sns.countplot(data=df, x='species', palette='YlOrRd')
plt.show()
sns.countplot(data=df, x='island', hue='species', palette='husl')
plt.show()
sns.pairplot(data=df, hue='species', palette='mako')
plt.show()
