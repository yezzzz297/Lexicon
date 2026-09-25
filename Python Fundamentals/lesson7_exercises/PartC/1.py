# Create a product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Notebook", 20)
print(product.name, product.price)
