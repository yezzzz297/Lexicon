from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])

client.close()
