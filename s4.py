import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/iris.csv")
print(data)
df=data.head(5)

s1=pd.Series(data['SepalLengthCm'])
print(s1)
print(s1.value_counts())
print(df)

d=pd.DataFrame(df['SepalLengthCm'])
print(d)

d1=pd.DataFrame(df['PetalLengthCm'])
print(d1)

d2=pd.concat([d,d1],axis=1)
print(d2)

