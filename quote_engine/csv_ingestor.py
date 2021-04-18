import pandas as pd

from quote_models import QuoteModel
from quote_engine.ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        csv = pd.read_csv(path)
        return [QuoteModel(**row) for index, row in csv.iterrows()]
