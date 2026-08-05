class IOCEnrichment:
    """
    IOC enrichment intelligence service.
    """

    def __init__(self):
        self.name = "IOC Enrichment Engine"


    def enrich(self, ioc):

        return {
            "ioc": ioc,
            "reputation": "unknown",
            "sources": [],
            "confidence": 0.0
        }


    def lookup(self, ioc):

        return self.enrich(ioc)