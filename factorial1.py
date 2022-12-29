def fact(num):
    
    assert (isinstance(num,int)),'Factorial is not defined for non integer.'
    assert (num>=0),'Factorial of negative number is not defined.' 
    if num==0:
        return 1
    else:
        return num*fact(num-1)
try:
    print(fact(12))
except Exception as obj:
    print(obj)

try:
    print(fact(12.45))
except Exception as obj:
    print(obj)

try:
    print(fact('today'))
except Exception as obj:
    print(obj)
