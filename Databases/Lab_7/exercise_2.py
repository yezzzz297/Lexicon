from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



orders = db.orders.find({"status": {"$ne": "delivered"}})

for order in orders:
    print(order["_id"], order["status"])

client.close()
