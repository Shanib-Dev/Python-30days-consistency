"Update Collection"
#You can update a record, or document as it is called in MongoDB, by using the update_one() method.
#The first parameter of the update_one() method is a query object defining which document to update.
#Note: If the query finds more than one record, only the first occurrence is updated.
#The second parameter is an object defining the new values of the document.
#Example
#Change the address from "Valley 345" to "Canyon 123":
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customer1"]

myquery = {"address":"Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"} }

mycol.update_one(myquery,newvalues)

for x in mycol.find():
    print(x)

"Update Many"
#To update all documents that meets the criteria of the query, use the update_many() method.
#Example
#Update all documents where the address starts with the letter "S":
myquery = {"address":{"$gt":"S"}}
newvalues = {"$set":{"name":"Minnie"}}
x = mycol.update_many(myquery, newvalues)
print(x.modified_count," documents updated")