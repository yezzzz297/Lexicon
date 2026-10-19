from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$match": {"status": {"$ne": "cancelled"}}},
    {"$unwind": "$items"},
    {"$lookup": {
        "from": "products",
        "localField": "items.product_id",
        "foreignField": "_id",
        "as": "product"
    }},
    {"$unwind": "$product"},
    {"$group": {"_id": "$product.category", "units_sold": {"$sum": "$items.quantity"}}}
]

for category in db.orders.aggregate(pipeline):
    print(category)

client.close()
