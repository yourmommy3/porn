import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="tester",
    database="flask"
)

#cur = mydb.cursor()
#cur.execute("CREATE DATABASE flask")

#cur = mydb.cursor()
#cur.execute("CREATE TABLE flask1(x int primary key,name text)")

cur = mydb.cursor()
cur.execute("insert into flask1 values(1,'name1')")
cur.execute("insert into flask1 values(2,'name2')")
cur.execute("insert into flask1 values(3,'name3')")

cur.execute("delete from flask1 where x=1")
cur.execute("update flask1 set name='satay' where x=2")


cur.execute("select * from flask1")

for i in cur:
    print(i)