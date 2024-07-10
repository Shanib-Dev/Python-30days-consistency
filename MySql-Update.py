import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)
mycursor=mydb.cursor()
sql="update customers set address='vasai 401208' where address='apple st 652'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"address changed")

#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated. If you omit the WHERE clause, all records will be updated!

"Prevent SQL Injection"
#It is considered a good practice to escape the values of any query, also in update statements.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module uses the placeholder %s to escape values in the update statement:
#Example
#Escape values by using the placeholder %s method:
sql = "update customers set address=%s where address=%s"
add = ('waliv','Park lane 38')
mycursor.execute(sql,add)
mydb.commit()
print(mycursor.rowcount,"address changed")