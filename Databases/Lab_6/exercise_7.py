from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

from pprint import pprint


result = db.customers.insert_one({
    "first_name": "Yetnayet",
    "last_name": "Belachew",
    "email": "yeti@example.com"
})
print(result.inserted_id)

customer = db.customers.find_one({"email": "yeti@example.com"})
pprint(customer)

client.close()
