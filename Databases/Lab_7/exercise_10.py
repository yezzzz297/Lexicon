from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]



order_filter = {
    "status": "new",
    "order_date": {"$lt": datetime(2026, 3, 20)}
}


count = db.orders.count_documents(order_filter)
print("Matching orders:", count)

result = db.orders.delete_many(order_filter)
print("Deleted orders:", result.deleted_count)

client.close()
