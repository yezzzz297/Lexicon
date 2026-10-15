from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]




product_filter = {"name": "Rain Jacket"}
db.products.update_one(
    product_filter,
    {
        "$addToSet": {"tags": "new"},
        "$set": {"restock_date": datetime.now()}
    }
)

product = db.products.find_one(product_filter)
print(product)

client.close()
