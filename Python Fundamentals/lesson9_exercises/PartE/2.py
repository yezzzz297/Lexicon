# Print a Product before adding __str__

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Notebook", 25)
print(product)
# The default output looks like <__main__.Product object at 0x...>.
# The address can change. It does not show the product name or price.
