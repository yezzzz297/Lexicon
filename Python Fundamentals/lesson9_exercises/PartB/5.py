# Print each title and its description

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


documents = [
    PDFDocument("Lab instructions"),
    TextDocument("Study notes"),
    PDFDocument("Report"),
    TextDocument("Shopping list"),
]

for document in documents:
    print(document.title, "-", document.describe())
