"Insert Into Table"
#To fill a table in MySQL, use the "INSERT INTO" statement.
#Example
#Insert a record in the "customers" table:
import  mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaikh@5155",
    database="mydata"
)


sql=("Insert into customers (name, address) Values ( %s, %s)")
val=("Sam", "Vasai 401208")

mycursor = mydb.cursor()
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted")

#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

"Insert Multiple Rows"
#To insert multiple rows into a table, use the executemany() method.
#The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
#Example
#Fill the "customers" table with data:
vall=[('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]
mycursor.executemany(sql, vall)
mydb.commit()
print(mycursor.rowcount, "was inserted")

"Get Inserted ID"
#You can get the id of the row you just inserted by asking the cursor object.
#Note: If you insert more than one row, the id of the last inserted row is returned.
#Example
#Insert one row, and return the ID:
val = ("Rehan", "waliv")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted and ID:", mycursor.lastrowid)