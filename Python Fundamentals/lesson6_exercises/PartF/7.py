
products = [
    {"name": "Laptop", "inventory": 4800},
    {"name": "Mouse", "inventory": 450},
    {"name": "Book", "inventory": 240},
]

for rank, product in enumerate(products, start=1):
    print(f"Rank {rank}: {product['name']} - inventory {product['inventory']}")
