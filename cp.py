import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df= pd.read_csv("imbddataset.csv")
df.head(3)
df.tail(3)
df.info()
df.isnull.sum()
subsetdf=df.iloc[40:75]
subsetdf
highest_vote=df.loc[df['Votes'].idxmax()]
highest_vote

plt.figure(figsize=(6,4))
sns.boxplot(x=df['IMBD_Rating'],y=df['RunTime'])
plt.xlabel("IMBD Rating")
plt.ylabel("IMBD Rating vs Runtime")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["IMBD_Rating"],bins=10)
plt.title("IMBD Rating")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Runtime_Rating"],bins=10)
plt.title("Runtime Rating")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Rating",data=df)
plt.title("Count Plot of Movie Ratings")
plt.xticks(rotation=45)
plt.show()