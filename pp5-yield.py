def squares(x=0):
    while x<10:
        x=x+1
        yield x*x

yieldedList=[i for i in squares()]
print(yieldedList)

yieldedList=list(squares())
print(yieldedList)



##output:
##    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
