from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

pipeline = [
    {"$group": {
        "_id": "$category",
        "cheapest": {"$min": "$price"},
        "most_expensive": {"$max": "$price"}
    }}
]

for category in db.products.aggregate(pipeline):
    print(category)

client.close()
