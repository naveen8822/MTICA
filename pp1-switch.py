def printBlue():
    print('you choose blue!\n')
    return
def printRed():
    print('you choose red!\n')
    
def printOrange():
    print('you choose Orange!\n')
    
def printYellow():
    print('you choose Orange!\n')

def printGreen():
    print('you choose Green!\n')

def choice():
    print('0:Blue')
    print('1:Red')
    print('2:Orange')
    print('3:Yellow')
    print('4:Green')
    print('5:Quit')
    return
ColorSelect={0:printBlue,1:printRed,2:printOrange,3:printYellow,4:printGreen}
selection=0
while True:
    if selection ==5:break
    choice()
    selection=int(input('select a option:'))
    if (selection>=0)and(selection<5):
        ColorSelect[selection]()
