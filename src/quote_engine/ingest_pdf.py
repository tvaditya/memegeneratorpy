import os
import subprocess

from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.ingest_txt import TextIngestor


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text_file = './pdf_to_text.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)
        return quotes
