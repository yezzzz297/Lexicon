from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$group": {"_id": "$city", "customers": {"$sum": 1}}},
    {"$sort": {"customers": -1}}
]

for city in db.customers.aggregate(pipeline):
    print(city)

client.close()
