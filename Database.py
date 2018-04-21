import sqlite3

db=sqlite3.connect('mydb1.db')
#for mysql
#conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='root123',db=mydb1.db)
cursor=db.cursor()
db.execute('create table if not exists mytable(id int,name text,sal int)')
id1=10
name1="Lucy"
sal1=30000
cursor.execute('''INSERT INTO mytable(id,name,sal)
VALUES(?,?,?)''',(id1,name1,sal1))

mydata=[(20,'Deepa',23456),(30,'Ashi',33333),(40,'Ragz',23764)]
cursor.executemany('''INSERT INTO mytable(id,name,sal) VALUES(?,?,?)''', mydata)

db.commit()

cursor.execute('''SELECT * FROM mytable''')
mydata1 = cursor.fetchone() #retrive the first row
print(mydata1)

print(mydata1[0],mydata1[1],mydata1[2])
all_rows=cursor.fetchall()
for row in all_rows:
    print('{0} : {1} : {2}'.format(row[0],row[1],row[2]))
cursor.execute('''UPDATE mytable SET sal = ? WHERE id = ? ''',(3463,id1))
db.commit()

cursor.execute('''SELECT * FROM mytable''')
all_rows=cursor.fetchall()
for row in all_rows:
    print('{0} : {1} : {2}'.format(row[0],row[1],row[2]))

cursor.execute('''DELETE FROM mytable WHERE id = ?''',(10,))
db.commit()
cursor.execute('''SELECT * FROM mytable''')
all_rows=cursor.fetchall()
for row in all_rows:
    print('{0} : {1} : {2}'.format(row[0],row[1],row[2]))
