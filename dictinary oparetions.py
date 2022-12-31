
dict={'name':'naveen','age':23,'Class':'first'}
print(dict)
{'name': 'naveen', 'age': 23, 'Class': 'first'}

print(dict['name'])
naveen
print(dict['age'])
23
print(dict['Class'])
first
dict['age']=25
dict
{'name': 'naveen', 'age': 25, 'Class': 'first'}
dict['course']='MCA'

dict
{'name': 'naveen', 'age': 25, 'Class': 'first', 'course': 'MCA'}
print(dict)
{'name': 'naveen', 'age': 25, 'Class': 'first', 'course': 'MCA'}
del dict['age']
dict
{'name': 'naveen', 'Class': 'first', 'course': 'MCA'}
dict.keys()
dict_keys(['name', 'Class', 'course'])
dict.values()
dict_values(['naveen', 'first', 'MCA'])
dict.items()
dict_items([('name', 'naveen'), ('Class', 'first'), ('course', 'MCA')])
for i in dict



for i in dict.values():print(dict)

{'name': 'naveen', 'Class': 'first', 'course': 'MCA'}
{'name': 'naveen', 'Class': 'first', 'course': 'MCA'}
{'name': 'naveen', 'Class': 'first', 'course': 'MCA'}
for i in dict.values():print(i)

naveen
first
MCA
for i in dict.items():print(i)

('name', 'naveen')
('Class', 'first')
('course', 'MCA')
for i in dict.keys():print(i)

name
Class
course
for i,j in dict.items():print9i,j)
SyntaxError: unmatched ')'
for i,j in dict.items():print(i,j)

name naveen
Class first
course MCA
