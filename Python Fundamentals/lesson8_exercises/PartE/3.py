# Create a laptop using super()

class Device:
    def __init__(self, brand, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        self.brand = brand
        self.year = year
        self.is_active = True


class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb


laptop = Laptop("Lenovo", 2024, 16)
print(laptop.brand, laptop.year, laptop.ram_gb, laptop.is_active)
