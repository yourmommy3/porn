import sqlite3

con = sqlite3.connect("lab.db")

#con.execute("create table labby(x int primary key,t text)")
con.execute("insert into labby values(1,'text1')")

cur = con.execute("select * from labby")

for i in cur:
    print(i)