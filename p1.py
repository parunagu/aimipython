import numpy as np
a=np.array([[1,2,4],[7,8,6]])
print(a)
print("number of dimensions",a.ndim)
print("sum of array",a.sum())
print("max of array",a.max())
print("sum of axis",a.sum(axis=1))
print("min of array",a.min())
print("max of axis",a.max(axis=1))
print("min of axis",a.min(axis=1))
print("cumsum of array",a.cumsum())
print("t of array",a.T)

import numpy as np
a=np.array([[1,2,4]])
b=np.array([[12,3,4]])
print(a)
print(b)

print("sum of 2 array",a+b)
print("sub of 2 array",a-b)
print("mul of 2 array",a*b)
print("div of 2 array",a/b)
