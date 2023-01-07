def reverseString(s):
    ans=[i[::-1]for i in s]
    return ans

inp=input().strip().split()
print(*reverseString(inp))


