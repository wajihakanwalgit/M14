import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("Tips Dataset.csv")
df.head()
sns.displot(df['size'])
sns.displot(df['tip'])
sns.displot(df['total_bill'])
sns.displot(df['total_bill'],kde= False)
sns.scatterplot(data=df,x="total_bill",y="tip",hue="time",style="time")
sns.pairplot(df,hue='time')
