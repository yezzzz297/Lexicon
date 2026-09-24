
product_names = ["Laptop", "Mouse", "Book"]
inventory_values = [4800, 450, 240]

for name, value in zip(product_names, inventory_values):
    print(f"{name}: inventory value = {value}")
