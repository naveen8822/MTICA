class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mult(self):
        return self.num1*self.num2
    def div(self):
        assert (self.num2!=0), 'number is divisible by 0'
        return self.num1/self.num2

n1=int(input())
n2=int(input())
obj=Number(n1,n2)

try:
    print(n1,'/',n2,'=',obj.div(),sep='')
except AssertionError as a:
    print(a)
print(n1,'+',n2,'=',obj.add(),sep='')
print(n1,'-',n2,'=',obj.sub(),sep='')
print(n1,'*',n2,'=',obj.mult(),sep='')



