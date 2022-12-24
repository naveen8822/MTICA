import math
r=int(input("Enter radius of cylinder : "))
h=int(input("Enter height of cylinder : "))
Vol=round(math.pi*r**2*h,4)
SA=round(2*math.pi*r**2+2*math.pi*r*h,4)
print(Vol,"\n"+str(SA))
