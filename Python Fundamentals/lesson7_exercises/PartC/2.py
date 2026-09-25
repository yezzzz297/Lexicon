# Share a class attribute

class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Notebook", 20)
product2 = Product("Pen", 10)
print(product1.tax_rate, product2.tax_rate)
