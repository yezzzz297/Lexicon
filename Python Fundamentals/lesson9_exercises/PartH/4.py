# Override export() to handle the same data differently

class Exporter:
    def export(self, data):
        return f"Data: {data}"


class ConsoleExporter(Exporter):
    def export(self, data):
        return f"Console output: {data}"


class TextExporter(Exporter):
    def export(self, data):
        text = ""
        for item in data:
            text += str(item) + "\n"
        return text


class SummaryExporter(Exporter):
    def export(self, data):
        return f"Summary: {len(data)} items"


data = ["Ada", "Grace", "Adam"]
print(ConsoleExporter().export(data))
print(TextExporter().export(data))
print(SummaryExporter().export(data))
