# Create three Exporter subclasses


class Exporter:
    def export(self, data):
        return f"Data: {data}"


class ConsoleExporter(Exporter):
    pass


class TextExporter(Exporter):
    pass


class SummaryExporter(Exporter):
    pass
