# Create a CPU class

class CPU:
    def __init__(self, model):
        self.model = model

cpu = CPU("Intel Core i5")
print(cpu.model)
