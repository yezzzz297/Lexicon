# Give one product its own tax rate

class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

products = [Product("Notebook", 20), Product("Pen", 10), Product("Bag", 100)]

products[0].tax_rate = 0.05
print("First product:", products[0].tax_rate)
print("Second product:", products[1].tax_rate)
print("Product class:", Product.tax_rate)
