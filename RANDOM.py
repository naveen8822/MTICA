from random import *
print(random())
print(randint(1,100))
print(uniform(10,20))


items=[1,2,3,4,5,6,7,8,9,0]
shuffle(items)
print(items)


items=[1,2,3,4,5,6,7,8,9,0]
x=sample(items,3)
print("x",x)
print(x[0])


y=sample(items,3)
print(y)



import sys
print(sys.version)
print(sys.version_info)
dir(sys)
