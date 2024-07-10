"Delete a Table"
#You can delete an existing table by using the "DROP TABLE" statement:
#Example
#Delete the table "customers":
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)
mycursor = mydb.cursor()
sql="drop table customer1"
mycursor.execute(sql)

"Drop Only if Exist"
#If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.
#Example
#Delete the table "customers" if it exists:
sql = "drop table if exists customer1"
mycursor.execute(sql)