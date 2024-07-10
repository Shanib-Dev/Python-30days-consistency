"Select From a Table"
#To select from a table in MySQL, use the "SELECT" statement:
#Example
#Select all records from the "customers" table, and display the result:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)

mycursor=mydb.cursor()
mycursor.execute("Select * from customers")
myresult = mycursor.fetchall()
for x in myresult:
   print(x)

#Note: We use the fetchall() method, which fetches all rows from the last executed statement.

"Selecting Columns"
#To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
#Example
#Select only the name and address columns:
mycursor.execute("Select name,address from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"Using the fetchone() Method"
#If you are only interested in one row, you can use the fetchone() method.
#The fetchone() method will return the first row of the result:
#Example
#Fetch only one row:
mycursor.execute("Select * from customers")
myresult=mycursor.fetchone()
for x in myresult:
    print(x)

