# Override describe() in each subclass

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "A general document"


class PDFDocument(Document):
    def describe(self):
        return "A PDF document with a fixed layout"


class TextDocument(Document):
    def describe(self):
        return "A plain text document"


print(PDFDocument("Report").describe())
print(TextDocument("Notes").describe())
