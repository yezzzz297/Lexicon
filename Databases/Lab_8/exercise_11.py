from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

import json


def find_orders(request_text):
    try:
        data = json.loads(request_text)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, dict):
        return []
    status = data.get("status")
    if not isinstance(status, str):
        return []
    return list(db.orders.find({"status": status}))


print(len(find_orders('{"status": "new"}')))
print(len(find_orders('{"status": {"$ne": "x"}}')))

client.close()
