from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

from pymongo.errors import ServerSelectionTimeoutError

wrong_client = MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=2000)

try:
    print(wrong_client["webshop"].products.count_documents({}))
except ServerSelectionTimeoutError:
    print("Cannot connect to the database. Please check that MongoDB is running.")
finally:
    wrong_client.close()

print(db.products.count_documents({}))

client.close()
