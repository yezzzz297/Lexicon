# Create the Exporter base class

class Exporter:
    def export(self, data):
        return f"Data: {data}"


exporter = Exporter()
print(exporter.export(["Ada", "Grace", "Adam"]))
