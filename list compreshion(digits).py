inp=input()
ans=[]
for i in inp:
    if i in '0123456789':
        ans.append(i)
print(*ans)

print(*[i for i in inp if i in '0123456789'])
