# Print three Product objects

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Price: {self.price}"

products = [
    Product("Notebook", 25),
    Product("Pen", 10),
    Product("Bag", 150),
]

for product in products:
    print(product)
