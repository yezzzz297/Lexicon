# Print three prices with tax

class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

products = [Product("Notebook", 20), Product("Pen", 10), Product("Bag", 100)]

for product in products:
    print(product.name, product.price_with_tax())
