fo=open(r'D:\PythonPractice_39\DAY10\filecreation.txt',"a+")
for i in range(6):
    inpstr=input('Enter String:')
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
