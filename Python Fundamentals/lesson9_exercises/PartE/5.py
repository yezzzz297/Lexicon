# Convert a Product to a string


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Price: {self.price}"


product = Product("Notebook", 25)
text = str(product)
print(text)
print(type(text))  # <class 'str'>
