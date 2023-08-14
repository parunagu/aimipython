import pandas as pd
import numpy as np

d={"days":[1,2,3,4,5,6,7,8,9,10],"steps":[4335,9992,7332,5404,5335,7552,8332,6504,8965,7689]}

df=pd.DataFrame(d)
print(d)
df["steps"]=df["steps"]+1000
print(df)
s=df[df["steps"]>7000]["days"]
print(list(s))
