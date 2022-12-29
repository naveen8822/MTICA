def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecresing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None



inpch=input("enter a ch:")
inpNum=int(input("enter a no:"))
printSeriesIncreasing(inpch,inpNum)
print('-'*50)
printSeriesDecresing(inpch,inpNum)
