num1=input("enter a number:")
num2=input("enter a number:")

try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print('Exception handled by N')
except ValueError:
    print('Exception handled by A')
except Exception as obj:
    print(obj)
else:
    print(num1,'/',num2,'=',res)
finally:
    print('Thanks')
print('visit again at python class at MTICA')
