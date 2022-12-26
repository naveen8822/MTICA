def count_consonent(s):
    consonent=0
    for i in s:
        if i in 'BCDEFGHJKLMNOPQRSTVWXYbcdefghjklmnopqrstvwxyz':
            consonent+=1
    return consonent
str1=input()
a=count_consonent(str1)
print("no of consonents in:'",str1,"'is",a)
