# Calculate the price with tax

class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

product = Product("Notebook", 20)
print(product.price_with_tax())
