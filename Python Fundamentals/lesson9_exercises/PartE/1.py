# Create a Product with name and price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Notebook", 25)
print(product.name, product.price)
