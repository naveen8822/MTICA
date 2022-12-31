import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute('SELECT * FROM cars')
rows=cur.fetchall()
##print(rows)

##for row in rows:
##    print(row)



for row in rows:
    print("{0:<15}|{1:<15}|{2:>15}".format(row[0],row[1],row[2]))
