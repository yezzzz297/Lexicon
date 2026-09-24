
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Monitor": 350,
    "Keyboard": 80,
    "Headphones": 200,
}

threshold = 300
cheap_products = {name: price for name, price in products.items() if price < threshold}
print(cheap_products)
