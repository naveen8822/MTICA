L1=input().split()
L2=input().split()
print(*[int(i)+int(j) for i,j in zip(L1,L2)])
