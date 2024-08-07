"Join Two or More Tables"
#You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
#Consider you have a "users" table and a "products" table:
#users
""""
users
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}
products
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }
"""
#These two tables can be combined by using users' fav field and products' id field.
#Example
#Join users and products to see the name of the users favorite product:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shaikh@5155",
  database="mydata"
)
mycursor = mydb.cursor()
sql =  "select \
        users.name as user, products.name as Favourite \
        from users INNER JOIN products on users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.

"LEFT JOIN"
#In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.
#If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
#Example
#Select all users and their favorite product:
sql = "select \
       users.name as user, products.name as Favourite \
       from users left join products on users.fav = products.id"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)

"RIGHT JOIN"
#If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
#Example
#Select all products, and the user(s) who have them as their favorite:
sql="select \
     users.name as user, products.name as Favourite \
     from users right join products on users.fav=products.id"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)

#Note: Hannah and Michael, who have no favorite product, are not included in the result.