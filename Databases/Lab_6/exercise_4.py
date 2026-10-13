from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


print(db.customers.count_documents({"city": "Uppsala"}))

client.close()
