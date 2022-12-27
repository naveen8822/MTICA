ans=[]
for i in range(1,1001):
    if '6' in str(i):
        ans.append(i)
print(ans)


print([i for i in range(1,1001) if '6' in str(i)])
