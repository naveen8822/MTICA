def printSeries(n,dn):
    if n<=12 and n>0:
        return dn[n]
    else:
        return "INVALID"

n=int(input())
dn={1:'jan',2:'feb',3:'march',4:'april',5:'may',6:'june',7:'july',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
print(printSeries(n,dn))
