import pandas as pd
import numpy as np

dict={ 'first score':[11,12,np.nan,13],
      'second score':[np.nan,11,12,13],
       'third score':[11,np.nan,12,13]}
data=pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-90))
print(data.dropna())
print(data.dropna(how="all"))


