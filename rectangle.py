class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'INVALID'
        self.length=length
        self.width=width

    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculateParameter(self):
        temp=2*(self.length*self.width)
        return temp
l=int(input())
w=int(input())

try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    para=ob.calculateParameter()

    print('Area of rectangle is',area)
    print('parameter of rectangle is ',para)
except AssertionError as obj:
    print(obj)
