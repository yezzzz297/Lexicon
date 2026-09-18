
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Mouse", "category": "electronics"},
    {"name": "Book", "category": "Books"},
    {"name": "Desk", "category": "Furniture"},
    {"name": "Notebook", "category": "Stationery"},
]

categories = {product["category"].lower() for product in products}
print(categories)
