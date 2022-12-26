def Checkanagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'YES'
    else:
        return'NO'
inp=input().split()
print(Checkanagram(inp[0],inp[1]))
