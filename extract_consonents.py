def extract_consonents(s):
    digit=''
    for i in s:
        if i in 'BCDFGHJKLMNOPQRSTVWXYbcdfghjklmnopqrstvwxyzZ':
            digit+=i
    return digit

str1=input()
a=extract_consonents(str1)
print("no of digits in:'",str1,"'is",a)
