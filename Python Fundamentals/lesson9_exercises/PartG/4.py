# Access the CPU through the Computer

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
