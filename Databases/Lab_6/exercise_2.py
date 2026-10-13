from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for customer in db.customers.find({"city": "Göteborg"}):
    print(customer["first_name"], customer["last_name"])

client.close()
