"Select With a Filter"
#When selecting records from a table, you can filter the selection by using the "WHERE" statement:
#Example
#Select record(s) where the address is "Park Lane 38": result:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)

mycursor=mydb.cursor()
mycursor.execute("Select * from customers where address='vasai 401208'")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

"Wildcard Characters"
#You can also select the records that starts, includes, or ends with a given letter or phrase.
#Use the %  to represent wildcard characters:
#Example
#Select records where the address contains the word "vas":
sql="select id from customers where address like '%vas%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"Prevent SQL Injection"
#When query values are provided by the user, you should escape the values.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module has methods to escape query values:
#Example
#Escape query values by using the placholder %s method:
sql = "select * from customers where address = %s"
add = ("vasai 401208",)
mycursor.execute(sql, add)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)