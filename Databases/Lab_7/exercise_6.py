from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



products = db.products.find(
    {},
    {"name": 1, "price": 1, "_id": 0}
).sort("price", 1).limit(5)

for product in products:
    print(product["name"], product["price"], "kr")

client.close()
