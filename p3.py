a=[1,2,3,4]
b=[3,5,7,8]
c=[6,8,3,5]
l=list(map(lambda a,b,c:a+b+c, a,b,c))
print(l)

lst=["mango","apple","orange","watermelon"]
l=list(filter(lambda x:"g" in x,lst))
print(l)
 
lst=["cat","table","pen","book","racchu","acchu","nagu"]
l1=list(filter(lambda x:"e" in x,lst))
print(l1)
