import numpy as np
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

print(df)

df.head(10)

df.tail(10)

df.shape

df.columns

df.index

df.values

df.info()

df.describe()

df1=df.dropna()
print(df1)

df2=df.isnull().sum()
print(df2)

df['Name'].fillna("omer",inplace=True)
df['Age'].fillna(0,inplace=True)
df['City'].fillna("delhi")

                  
