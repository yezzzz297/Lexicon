# Extend the base summary with super()

class Report:
    def get_summary(self):
        return "General report summary."


class SalesReport(Report):
    def get_summary(self):
        summary = super().get_summary()
        return summary + " Total sales: 1000."


report = SalesReport()
print(report.get_summary())
