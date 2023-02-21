import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'advancedpython')
mycursor = mydb.cursor()
sql = "insert into student (name,location) VALUES(%s, %s)"
val = [
    ("Mark","North Street"),
    ('peter','street 2'),
    ('rohan','East'),
    ('rahul','West')
    ]

mycursor.executemany(sql,val)

print(mycursor.rowcount,"record inserted.")