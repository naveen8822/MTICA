string='''practice problems for list compreshion in python.'''


ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
