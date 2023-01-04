def printJan():
    print('january')
    
def printFeb():
    print('February')
    
def printMar():
    print('March')
    
def printApl():
    print('April')
    
def printMay():
    print('May')

def printJun():
    print('June')

def printJul():
    print('July')

def printAug():
    print('august')

def printSep():
    print('September')

def printOct():
    print('October')

def printNov():
    print('November')
    
def printDec():
    print('December')
def choice():
    print('Select the month:')
MonthSelect={1:printJan,2:printFeb,3:printMar,4:printApl,5:printMay,6:printJun,7:printJul,8:printAug,9:printSep,10:printNov,11:printDec}
choice()
MonthNo=int(input())
if MonthNo>=1 and MonthNo<12:
    MonthSelect[MonthNo]()

else:
    print("INVALID")
