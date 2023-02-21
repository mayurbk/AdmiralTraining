import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',password='python', database = 'advancedpython')
mycursor = mydb.cursor()
sql = "UPDATE student SET location = 'West Street' WHERE location = 'North Street'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record updated successfully")