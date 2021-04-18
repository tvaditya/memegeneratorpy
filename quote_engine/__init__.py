import os

from quote_engine.ingestor_interface import IngestorInterface, ext
from quote_engine.text_ingestor import TextIngestor
from quote_engine.docx_ingestor import DocxIngestor
from quote_engine.pdf_ingestor import PDFIngestor
from quote_engine.csv_ingestor import CSVIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        filename, file_extension = os.path.splitext(path)
        if not cls.can_ingest(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == ext.get("TXT"):
            return TextIngestor.parse(path)
        if file_extension == ext.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == ext.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == ext.get("CSV"):
            return CSVIngestor.parse(path)
