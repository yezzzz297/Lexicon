# Pass a CPU object to Computer

class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


cpu = CPU("Intel Core i5")
computer = Computer("Lenovo", cpu)
