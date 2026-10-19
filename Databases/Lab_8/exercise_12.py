from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

def products_under(text):
    try:
        price = float(text)
    except ValueError:
        print("Please enter a number.")
        return []
    return list(db.products.find(
        {"price": {"$lt": price}},
        {"_id": 0, "name": 1, "price": 1}
    ))


for text in ["300", "abc", '{"$gt": 0}']:
    for product in products_under(text):
        print(product)

client.close()
