from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$project": {"_id": 1, "number_of_items": {"$size": "$items"}}}
]

for order in db.orders.aggregate(pipeline):
    print(order)

client.close()
