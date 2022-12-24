start=int(input("Enter starting range : "))
stop=int(input("Enter stopping range : "))
lis=[]
for i in range(start,stop+1):
    lis.append(i)
print(*lis)
print(sum(lis))
