import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python"
)

print(mydb)