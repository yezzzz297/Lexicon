# Store exporters in a list
# Reference: your overriding, polymorphism, duck typing and composition examples.

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
        # Build text with one item per line; no real file is needed.
        text = ""
        for item in data:
            text += str(item) + "\n"
        return text


class SummaryExporter(Exporter):
    def __str__(self):
        return "Summary exporter"

    def export(self, data):
        return f"Summary: {len(data)} items"


exporters = [
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter(),
]
