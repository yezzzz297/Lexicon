from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



customers = db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}})

for customer in customers:
    print(customer["first_name"], customer["last_name"], customer["city"])

client.close()
