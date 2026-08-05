class IntelligenceCoordinator:

    def __init__(self):
        self.sources = []


    def add_source(self, source):

        self.sources.append(source)

        return {
            "source": source,
            "added": True
        }


    def collect(self):

        return {
            "sources": self.sources,
            "status": "collected"
        }