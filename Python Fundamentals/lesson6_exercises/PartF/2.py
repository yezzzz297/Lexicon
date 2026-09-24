
products = [
    {"name": "  laptop  ", "category": "  electronics ", "price": 1200, "stock": 4},
    {"name": "Mouse", "category": "electronics", "price": 25, "stock": 18},
    {"name": "BOOK", "category": "books", "price": 20, "stock": 12},
]

cleaned = [
    {
        "name": product["name"].title(),
        "category": product["category"].lower(),
        "price": product["price"],
        "stock": product["stock"],
    }
    for product in products
]

print(cleaned)
