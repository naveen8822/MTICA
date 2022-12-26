def count_digits(s):
    n_digit=0
    for i in s:
        if i in '123456789':
            n_digit+=1
    return n_digit

str1=input()
a=count_digits(str1)
print("no of digits in:'",str1,"'is",a)
