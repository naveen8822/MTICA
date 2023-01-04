def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMul(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+:addition");print("-:subtraction");print("*:Multiplication");print("/:Division");print("q:Quit")
    return
colorSelect={"+":printAdd,"-":printSub,"*":printMul,"/":printDiv}
while True:
    choice()
    selection=input('select an arthmetic operation:')
    if selection=='q' or selection=='Q':break
    if ((selection=='+')or(selection=='-')or(selection=='*')or(selection=='/')):
        n1=int(input("enter first no:"))
        n2=int(input("enter second no:"))
        z=colorSelect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
