
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 18},
    {"name": "Book", "price": 20, "stock": 12},
]

inventory = {product["name"]: product["price"] * product["stock"] for product in products}
print(inventory)
