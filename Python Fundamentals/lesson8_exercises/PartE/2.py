# Add shared validation and state

class Device:
    def __init__(self, brand, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        self.brand = brand
        self.year = year
        self.is_active = True


device = Device("Apple", 2024)
print(device.brand, device.year, device.is_active)
