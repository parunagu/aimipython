import pandas as pd
import numpy as np
info=np.array([1,2,3])
print(info)

s=pd.Series(4,index=([0,1,2,3]))
print(s)

i=pd.Index([10,14,12,13])
print(i.value_counts())

