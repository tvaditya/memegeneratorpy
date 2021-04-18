from docx import Document

from quote_model import QuoteModel
from quote_engine.ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        document = Document(path)
        quotes = []
        for paragraph in document.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(" - ")))
        return quotes
