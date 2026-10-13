from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for order in db.orders.find():
    number_of_items = len(order["items"])
    print(f"Order {order['_id']}: {number_of_items} items")

client.close()
