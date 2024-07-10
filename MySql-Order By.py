"Sort the Result"
#Use the ORDER BY statement to sort the result in ascending or descending order.
#The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.
#Example
#Sort the result alphabetically by name: result:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)
mycursor=mydb.cursor()
sql = "select * from customers order by name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"ORDER BY DESC"
#Use the DESC keyword to sort the result in a descending order.
#Example
#Sort the result reverse alphabetically by name:
sql = "select * from customers order by name desc"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)