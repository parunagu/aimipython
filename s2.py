import pandas as pd
import numpy as np

ser1=pd.Series([10,12,11,11])
ser2=pd.Series([1,12,15,3,5])
 
u=pd.Series(np.union1d(ser1,ser2))
print("_______union_______",u)

i=pd.Series(np.intersect1d(ser1,ser2))
print("______intersect_______",i)

nc=u[~ u.isin(i)]
print("_____remove common number_____",nc) 
