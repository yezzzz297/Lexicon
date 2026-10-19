from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$group": {"_id": "$customer_id", "orders": {"$sum": 1}}},
    {"$match": {"orders": {"$gte": 2}}}
]

for customer in db.orders.aggregate(pipeline):
    print(customer)

client.close()
