"""Use the sort() method to sort the result in ascending or descending order."""
import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# # Sort the result alphabetically by name:
# mydoc = mycol.find().sort("name")
#
# for x in mydoc:
#   print(x)

# Sort the result reverse alphabetically by name:
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)