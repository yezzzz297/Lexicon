from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": {"product": "$_id", "tag": "$tags"}}},
    {"$group": {"_id": "$_id.tag", "products": {"$sum": 1}}},
    {"$sort": {"products": -1}}
]

for tag in db.products.aggregate(pipeline):
    print(tag)

client.close()
