import sys
print('Coming through stdout')


save_out=sys.stdout
fh=open(r'd:\PythonPractice_39\DAY17\test.txt',"w")
sys.stdout=fh
print("this line goes to test   txt")
print(input())
sys.stdout=save_stdout
fh.close()



