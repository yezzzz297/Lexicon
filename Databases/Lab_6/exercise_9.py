from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Exercise 9: show unknown when the city is missing.
for customer in db.customers.find():
    city = customer.get("city", "unknown")
    print(f"{customer['first_name']} {customer['last_name']} ({city})")

client.close()
