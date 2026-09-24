
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 18},
    {"name": "Book", "price": 20, "stock": 12},
    {"name": "Desk Lamp", "price": 80, "stock": 7},
]

sorted_by_inventory = sorted(
    products,
    key=lambda product: product["price"] * product["stock"],
    reverse=True,
)
print(sorted_by_inventory)
