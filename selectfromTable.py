#select the records from student table
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'advancedpython')
mycursor = mydb.cursor()

mycursor.execute("SELECT * from student")
result = mycursor.fetchmany()
for x in result:
    print(x)
print(result)