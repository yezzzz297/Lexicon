# Explain the HAS-A relationship
# Reference: your Car HAS-A Engine composition example.

class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


cpu = CPU("Intel Core i5")
computer = Computer("Lenovo", cpu)

print(computer.brand)
print(computer.cpu.model)

# A Computer HAS-A CPU: the CPU is one part inside the computer.
# A Computer is not a kind of CPU, so inheritance would not fit.
