# Override the report summary

class Report:
    def get_summary(self):
        return "General report summary."


class SalesReport(Report):
    def get_summary(self):
        return "Total sales: 1000."


report = SalesReport()
print(report.get_summary())
