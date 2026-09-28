# Create a device

class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


device = Device("Apple", 2024)
print(device.brand, device.year)
