import sqlite3

con = sqlite3.connect("emp.db")
#con.execute("create table EMP(id integer primary key autoincrement, name text not null, email text not null)")
#con.execute("insert into EMP values (1,'satay','123@gmail.com')")
#con.commit()    
cur = con.execute("select * from  EMP")
for row in cur: 
    print(row[0],row[1],row[2])
con.close()