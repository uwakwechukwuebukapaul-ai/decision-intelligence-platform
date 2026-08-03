from datetime import datetime


class EventIngestion:
    """
    Collects events from security sources.
    """


    def ingest(
        self,
        source,
        event
    ):

        return {

            "source":
                source,

            "event":
                event,

            "status":
                "ingested",

            "timestamp":
                datetime.utcnow().isoformat()

        }