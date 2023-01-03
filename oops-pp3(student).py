class Student:
    college='MTICA'
    course="MCA"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('name: '+self.name,'\nrollno: '+str(self.rollno))
        print('Collage: '+self.college,'\nCourse: '+self.course)

lstObj=[] 
for i in range(2):
    inp=input()
    r=int(input()) 
    temp='obj'+str(i)
    temp=Student(inp,r)
##    obj=Student(inp,r)
##    obj.displayStudent()
    lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
