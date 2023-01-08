import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("function name: {0}".format(sys.argv[0]))
       # print("function name: %s"%(sys.argv[0]))
        
    else:
        print("{0}.argument: {1}".format(i,sys.argv[i]))
       #print("%d.argument: %s"%(i,sys.argv[i]))



           
#output:
'''['D:/PythonPractice_39/DAY17/SYS.py']
function name: D:/PythonPractice_39/DAY17/SYS.py'''


##output:(cmd)
##D:\>python \PythonPractice_39\DAY17\SYS.py naveen mca
##['\\PythonPractice_39\\DAY17\\SYS.py', 'naveen', 'mca']
##function name: \PythonPractice_39\DAY17\SYS.py
##1.argument: naveen
##2.argument: mca
