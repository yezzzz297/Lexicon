from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



orders = db.orders.find({"items.product_id": 2})

for order in orders:
    print(order)

client.close()
