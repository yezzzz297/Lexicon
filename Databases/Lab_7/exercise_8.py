from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



product_filter = {"category": "Accessories"}
db.products.update_many(product_filter, {"$inc": {"price": 20}})

for product in db.products.find(product_filter):
    print(product["name"], product["price"], "kr")

client.close()
