class ThreatFeedConnector:
    """
    External threat intelligence feeds.
    """

    def __init__(self):
        self.name = "Threat Intelligence"

    def fetch_indicators(self):
        return {
            "indicators": [],
            "source": self.name
        }

    def enrich_ioc(self, indicator):
        return {
            "indicator": indicator,
            "reputation": "unknown"
        }