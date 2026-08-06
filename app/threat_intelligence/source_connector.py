class SourceConnector:

    def __init__(self, source_name="offline_feed"):
        self.source_name = source_name


    def query(self, ioc):

        return {
            "source": self.source_name,
            "ioc": ioc,
            "found": True,
            "confidence": 0.85
        }