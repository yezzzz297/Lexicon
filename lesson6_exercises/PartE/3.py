
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 350},
]

sorted_products = sorted(products, key=lambda product: product["price"])
print(sorted_products)
