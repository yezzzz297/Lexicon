# Create three laptops and change one price

class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price


laptop1 = Laptop("Lenovo", "ThinkPad", 16, 1200)
laptop2 = Laptop("Apple", "MacBook Air", 16, 1400)
laptop3 = Laptop("Dell", "Inspiron", 8, 700)
print("Original price:", laptop2.price)
laptop2.price = 1300
for laptop in [laptop1, laptop2, laptop3]:
    print(laptop.brand, laptop.model, laptop.ram_gb, laptop.price)
