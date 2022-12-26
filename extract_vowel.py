def extract_vowel(s):
    temp_vowel=''
    for i in s:
       # print("i=",i)
        if i in 'AEIOUaeiou':
            temp_vowel+=i
            #print("i:",i,"temp_vowel:",temp_vowel)
    return temp_vowel
str1=input()
a=extract_vowel(str1)
print('vowel:',a)



def extract_consonents(s):
    temp_consonents=''
    for i in s:
       # print("i=",i)
        if i in 'BCDFGHJKLMNOPQRSTUVWXYZbcdfghjklmnopqrstuvwxyz':
            temp_consonents+=i
            #print("i:",i,"temp_consonents:",temp_consonents)
    return temp_consonents
str1=input()
a=extract_consonents(str1)
print('consonents:',a)
