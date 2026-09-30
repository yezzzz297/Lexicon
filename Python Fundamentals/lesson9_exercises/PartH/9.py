# Inspect inheritance with isinstance()


class Exporter:
    def export(self, data):
        return f"Data: {data}"

    def __str__(self):
        return "General exporter"


class ConsoleExporter(Exporter):
    def __str__(self):
        return "Console exporter"

    def export(self, data):
        return f"Console output: {data}"


class TextExporter(Exporter):
    def __str__(self):
        return "Text exporter"

    def export(self, data):
        text = ""
        for item in data:
            text += str(item) + "\n"
        return text


class SummaryExporter(Exporter):
    def __str__(self):
        return "Summary exporter"

    def export(self, data):
        return f"Summary: {len(data)} items"


class CountExporter:
    def __str__(self):
        return "Count exporter (duck typing)"

    def export(self, data):
        return f"Number of records: {len(data)}"


exporters = [
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter(),
    CountExporter(),
]

data = ["Ada", "Grace", "Adam"]

for exporter in exporters:
    print(exporter)
    print(exporter.export(data))

print(isinstance(exporters[0], Exporter))  # True: 
print(isinstance(exporters[3], Exporter))  # False: 

