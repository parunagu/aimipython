#lambda,map,filter,reduce
a=lambda x:x+5
print(a(2))

b=lambda x,y:x+y
print(b(2,4))

c=lambda x,y:x if (x>y) else y
print(c(12,4)) 

d=lambda a:a*a
print(d(10))

#map
lst=[1,2,3,4,5]
l=list(map(lambda x:x+5,lst))
print(l)

#filter
#even number
lst=[1,2,3,4,5,6,7,8]
l=list(filter(lambda x:x%2,lst))
print(l)

#odd number
lst=[1,2,3,4,5,6,7,8]
l=list(filter(lambda x:x%1,lst))
print(l)
 
#reduce
lst=[1,2,3,4,5,6,7]
from functools import reduce
y=reduce(lambda x,y:x+y,lst)
print(y)

lst=[1,2,3,4,5,6,7]
from functools import reduce
y=reduce(lambda x,y:x-y,lst)
print(y)

lst=[1,2,3,4,5,6,7,4,9]
from functools import reduce
y=reduce(lambda a,b: a if (a>b) else b,lst)
print(y)

lst=[1,2,3,4]
from functools import reduce
y=reduce(lambda x,y:x*y,lst)
print(y)

lst=[1,2,3,4,5,6,7,4,9]
from functools import reduce
y=reduce(lambda a,b: a if (a<b) else b,lst)
print(y)
