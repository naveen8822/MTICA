string='''practice problems for list compreshion in python.'''

ans=[]
for i in string:
    if i not in 'AEIOUaeiou':
        ans.append(i)
print(*ans)

##ans=[i for i in string if i not in 'AEIOUaeiou']
##print(*ans)

##print(*[i for i in string if i not in 'AEIOUaeiou'])
##
