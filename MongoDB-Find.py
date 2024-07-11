"Find One"
#To select data from a collection in MongoDB, we can use the find_one() method.
#The find_one() method returns the first occurrence in the selection.
#Example
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabase"]
mycol=mydb["customer1"]
x = mycol.find_one()
print(x)

"Find All"
#To select data from a table in MongoDB, we can also use the find() method.
#The find() method returns all occurrences in the selection.
#The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
#No parameters in the find() method gives you the same result as SELECT * in MySQL.
#Example
#Return all documents in the "customers" collection, and print each document:

for x in mycol.find():
    print(x)

"Return Only Some Fields"
#The second parameter of the find() method is an object describing which fields to include in the result.
#This parameter is optional, and if omitted, all fields will be included in the result.
#Example
#Return only the names and addresses, not the _ids:
for x in mycol.find({},{"_id":1 , "name": 1, "address": 1}):
    print(x)

#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa:
#Example
#This example will exclude "address" from the result:
for x in mycol.find({},{ "address": 0 }):
  print(x)

#Example
#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)