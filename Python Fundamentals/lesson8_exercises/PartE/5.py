# Both subclasses use the shared initialization

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


class Phone(Device):
    def __init__(self, brand, year, storage_gb):
        super().__init__(brand, year)
        self.storage_gb = storage_gb


laptop = Laptop("Lenovo", 2024, 16)
phone = Phone("Apple", 2024, 128)
print(laptop.brand, laptop.year, laptop.is_active)
print(phone.brand, phone.year, phone.is_active)

# Both subclasses use the year validation in Device.
try:
    Laptop("Lenovo", -1, 16)
except ValueError as error:
    print(error)

try:
    Phone("Apple", -1, 128)
except ValueError as error:
    print(error)
