class IngestionEngine:
    """
    Core ingestion controller.
    """

    def __init__(self):
        self.events = []

    def ingest(self, event):

        self.events.append(event)

        return {
            "status": "accepted",
            "event_id": len(self.events)
        }

    def count(self):
        return len(self.events)