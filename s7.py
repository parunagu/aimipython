import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic.csv",index_col=["PassengerId"])
print(data)

print(data.info())
print(data.shape)

print(data.head(5))
print(data.tail(10))

print(data.loc[data['Age']>15])
print(data.iloc[11:20])

