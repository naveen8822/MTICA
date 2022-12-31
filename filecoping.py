fo1=open(r'D:\PythonPractice_39\DAY10\filecreation.txt',"r")
fo2=open(r'D:\PythonPractice_39\DAY10\fILECOPY.txt',"w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file copied")
