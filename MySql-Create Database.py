"Creating a Database"
#To create a database in MySQL, use the "CREATE DATABASE" statement:
#Example
#create a database named "mydatabase":
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shaikh@5155"
)

mycursor = mydb.cursor()
#mycursor.execute("create database mydata")

#If the above code was executed with no errors, you have successfully created a database.

"Check if Database Exists"
#You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:
#Example
#Return a list of your system's databases:
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

#Or you can try to access the database when making the connection:
#Example
#Try connecting to the database "mydata":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shaikh@5155",
  database="mydata"
)

#If the database does not exist, you will get an error.