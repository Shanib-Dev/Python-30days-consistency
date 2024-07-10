"Limit the Result"
#You can limit the number of records returned from the query, by using the "LIMIT" statement:
#Example
#Select the 5 first records in the "customers" table:
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)
mycursor=mydb.cursor()
sql = "select * from customers limit 5"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"Start From Another Position"
#If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
#Example
#Start from position 3, and return 5 records:
sql ="select * from customers limit 5 offset 2"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)