import datetime
ob=datetime.datetime.now()

str1=str(ob.day)+' - '+str(ob.month)+' - '+str(ob.year)
str2=str(ob.hour)+' - '+str(ob.minute)+' - '+str(ob.second)
str3='backup_'+str1+' - '+str2+'.db'
print(str3)
