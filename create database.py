import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root', password = 'python')
mycursor = mydb.cursor()
mycursor.execute("create database trainingsessions")
print("databases created successfully.")
mycursor.execute("Show Databases")
for x in mycursor:
    print(x)





#checking the database created in the above code


# import mysql.connector
# mydb = mysql.connector.connect(host='localhost',user= 'root', password = 'python')
# mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#      print(x)



