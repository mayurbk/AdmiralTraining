
#create a table name student
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'trainingsessions')
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE student(name VARCHAR(20), location VARCHAR(20))')
print("table created")
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)
#checking the existence of the table






# import mysql.connector
#
# mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'advancedpython')
# mycursor = mydb.cursor()
# mycursor.execute('SHOW TABLES')
# for i in mycursor:
#     print(i)