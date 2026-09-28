# Create a phone using super()

class Device:
    def __init__(self, brand, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        self.brand = brand
        self.year = year
        self.is_active = True


class Phone(Device):
    def __init__(self, brand, year, storage_gb):
        super().__init__(brand, year)
        self.storage_gb = storage_gb


phone = Phone("Apple", 2024, 128)
print(phone.brand, phone.year, phone.storage_gb, phone.is_active)
