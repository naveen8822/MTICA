inpStr=int(input("Enter a number : "))
n=str(inpStr)
if int(n[::-1])==inpStr:
    print(inpStr,"is palindrome")
else:
    print(inpStr,"is not palindrome")
