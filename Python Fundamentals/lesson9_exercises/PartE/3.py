# Make Product easy to read with __str__


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Price: {self.price}"


product = Product("Notebook", 25)
print(product)
