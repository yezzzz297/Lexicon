from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for customer in db.customers.find():
    city = customer.get("city", "unknown")
    print(f"{customer['first_name']} {customer['last_name']} ({city})")

client.close()
