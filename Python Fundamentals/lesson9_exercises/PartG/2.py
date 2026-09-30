# A Computer contains a CPU object


class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu
