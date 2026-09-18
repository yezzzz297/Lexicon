
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Book", "price": 20, "stock": 12},
    {"name": "Desk Lamp", "price": 80, "stock": 7},
]

in_stock = [product for product in products if product["stock"] > 0]
print(in_stock)
