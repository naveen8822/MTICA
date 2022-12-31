import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS cars')
cur.execute('''CREATE TABLE    cars(id INT,Name TEXT,Price INT)''')
print('table cars created.')
cur.execute("INSERT INTO cars VALUES(1,'audi',50000)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',55000)")
cur.execute("INSERT INTO cars VALUES(3,'skoda',60000)")
cur.execute("INSERT INTO cars VALUES(4,'vlovo',58000)")
cur.execute("INSERT INTO cars VALUES(5,'bently',40000)")
cur.execute("INSERT INTO cars VALUES(6,'citrogen',53400)")
cur.execute("INSERT INTO cars VALUES(7,'volkswagen',100000)")

con.commit()
print("values in table car inserted.")

