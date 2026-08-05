class IntelligenceCoordinator:
    """
    Coordinates threat intelligence operations inside autonomous SOC.
    """

    def __init__(self):
        self.intelligence_sources = []

    def collect_intelligence(self, source):
        self.intelligence_sources.append(source)

        return {
            "source": source,
            "status": "collected"
        }

    def get_sources(self):
        return self.intelligence_sources