import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/iris.csv")[:149]
print(data)

print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-67))
print(data.dropna())
print(data.dropna(how="all"))
