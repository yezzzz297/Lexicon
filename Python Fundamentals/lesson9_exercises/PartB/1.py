# Create the Document base class


class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "A general document"


document = Document("Notes")
print(document.title)
print(document.describe())
