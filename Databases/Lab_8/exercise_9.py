from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$unwind": "$items"},
    {"$group": {
        "_id": "$status",
        "revenue": {"$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}}
    }}
]

for status in db.orders.aggregate(pipeline):
    print(status)

client.close()
