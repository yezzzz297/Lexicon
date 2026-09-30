# Inherit from Document

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "A general document"


class PDFDocument(Document):
    pass


class TextDocument(Document):
    pass


print(PDFDocument("Report").title)
print(TextDocument("Notes").title)
