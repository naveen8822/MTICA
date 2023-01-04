def printSunday():
    print('Sunday \n')
def printMonday():
    print('Monday\n')
def printTuesday():
    print('tuesday \n')
def printWednesday():
    print('wenesday \n')
def printThursday():
    print('thursday \n')
def printFriday():
    print('Friday \n')
def printSaturday():
    print('Saturday \n')
def choose():
    print('Enter a number between 1-7')
daySelect={1:printSunday,2:printMonday,3:printTuesday,4:printWednesday,5:printThursday,6:printFriday,7:printSaturday}
choose()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    daySelect[dayNo]()
else:
    print("INVALID")
