"Creating a Table"
#To create a table in MySQL, use the "CREATE TABLE" statement.
#Make sure you define the name of the database when you create the connection
#Example
#Create a table named "customers":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shaikh@5155",
  database="mydata"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name varchar(260), address varchar(260))")

#If the above code was executed with no errors, you have now successfully created a table.

"Check if Table Exists"
#You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
#Example
#Return a list of your system's databases:
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

"Primary Key"
#When creating a table, you should also create a column with a unique key for each record.
#This can be done by defining a PRIMARY KEY.
#We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.
#Example
#Create primary key when creating the table:
mycursor.execute("create table customer1(ID int auto_increment primary key, name varchar(255), address varchar (255))")


"If the table already exists, use the ALTER TABLE keyword:"
#Example
#Create primary key on an existing table:"
mycursor.execute("alter table customers add column id int auto_increment primary key")
