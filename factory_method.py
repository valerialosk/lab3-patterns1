from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

class WordDocument(Document):
    def open(self):
        return "Opening Word document"

class PDFDocument(Document):
    def open(self):
        return "Opening PDF document"