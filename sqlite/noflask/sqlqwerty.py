import sqlite3

con = sqlite3.connect('employee.db')

#con.execute("CREATE TABLE TEMP(i int primary key,name text)")

con.execute("insert into TEMP values(1,'satay')")
con.execute("insert into TEMP values(2,'qwert')")
con.execute("insert into TEMP values(3,'xcvd')")

cur = con.execute("SELECT * from TEMP")

for row in cur:
    print(row)

    
