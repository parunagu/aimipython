import pandas as pd
import numpy as np

data=pd.DataFrame([[10,11,12,13],[23,34,45,67]] ,columns=["maths","science","kannada","pms"])
print(data)
print(data.sum())
print(data.min())
print(data.max())
print(data.cumsum())
print(data["maths"].sum())
print(data["pms"].min())
print(data["kannada"].max())
print(data["science"].value_counts())
print(data.agg[sum,min.max])


