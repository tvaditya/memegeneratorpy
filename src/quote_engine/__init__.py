import os

from ingestors.ingestor_interface import IngestorInterface, ext
from ingestors.ingest_txt import TextIngestor
from ingestors.ingest_docx import DocxIngestor
from ingestors.ingest_pdf import PDFIngestor
from ingestors.ingest_csv import CSVIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        filename, file_extension = os.path.splitext(path)
        if not cls.verify(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == extensions.get("TXT"):
            return TextIngestor.parse(path)
        if file_extension == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == extensions.get("CSV"):
            return CSVIngestor.parse(path)
