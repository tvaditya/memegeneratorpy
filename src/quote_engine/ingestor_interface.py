ext = { "CVS":".csv", "DOCX":".docs", "PDF":".pdf", "TXT":".txt" }

class IngestorInterface :
    @classmethod
    def verify(cls, file_ext):
        return file_ext in ext.values()

    @classmethod
    def parse(cls,path):
        pass
