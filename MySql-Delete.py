"Delete Record"
#You can delete records from an existing table by using the "DELETE FROM" statement:
#Example
#Delete any record where the address is "Mountain 21":
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)
mycursor=mydb.cursor()
sql="delete from customers where address = 'vasai 401208'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!

"Prevent SQL Injection"
#It is considered a good practice to escape the values of any query, also in delete statements.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module uses the placeholder %s to escape values in the delete statement:
#Example
#Escape values by using the placeholder %s method:
sql="delete from customers where name = %s"
add= ("Rehan",)
mycursor.execute(sql,add)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")