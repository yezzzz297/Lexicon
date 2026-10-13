from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


product = db.products.find_one({"name": "Sandals"})
print(product["stock"])

client.close()
