from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


for product in db.products.find():
    print(product["name"], "costs", product["price"], "kr")

client.close()
