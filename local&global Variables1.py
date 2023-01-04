def add(n1,n2):
    temp=n1+n2
    global a,b
    a+=10
    print('output of globals:',globals())
    print('output of locals:',locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)




##
##output:
##
##11
##12
##output of globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
##                    '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
##                    '__file__': 'D:/PythonPractice_39/DAY13/local&global Variables1.py', 'add': <function add at 0x0000025856EB1120>,
##                    'a': 21, 'b': 12}

##output of locals: {'n1': 11, 'n2': 12, 'temp': 23}
##21 + 12 = 23
