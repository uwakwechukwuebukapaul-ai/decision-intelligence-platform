class SIEMConnector:
    """
    SIEM integration abstraction.

    Future integrations:
    - Microsoft Sentinel
    - Splunk
    - Elastic
    - Google SecOps
    """

    def __init__(self):
        self.name = "SIEM"

    def ingest_events(self, events):
        return {
            "connector": self.name,
            "events_received": len(events),
            "status": "processed"
        }

    def query(self, query):
        return {
            "query": query,
            "results": []
        }