from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


result = db.products.insert_many([
    {"_id": 13, "name": "Scarf", "category": "Accessories",
     "price": 299, "stock": 15, "tags": ["winter"],
     "details": {"color": "red"}},
    {"_id": 14, "name": "Gloves", "category": "Accessories",
     "price": 199, "stock": 20, "tags": ["winter"],
     "details": {"color": "black"}}
])
print(db.products.count_documents({}))

client.close()
