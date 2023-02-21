import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'advancedpython')
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE courses(name VARCHAR(20), duration VARCHAR(20))')