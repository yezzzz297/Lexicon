from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

products = db.products.find({"price": {"$gt": 1000}})

for product in products:
    print(product["name"], product["price"], "kr")

client.close()
