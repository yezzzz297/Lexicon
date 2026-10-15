from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]




products = db.products.find(
    {"tags": "sport"},
    {"name": 1, "tags": 1, "_id": 0}
)

for product in products:
    print(product)

client.close()
