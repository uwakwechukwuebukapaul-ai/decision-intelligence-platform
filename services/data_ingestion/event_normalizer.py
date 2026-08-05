from datetime import datetime


class EventNormalizer:
    """
    Converts different security formats
    into Sentinel DNA standard events.
    """

    def normalize(self, event):

        return {
            "timestamp": event.get(
                "timestamp",
                datetime.utcnow().isoformat()
            ),
            "source": event.get("source", "unknown"),
            "severity": event.get("severity", "medium"),
            "entity": event.get("entity"),
            "indicators": event.get("indicators", []),
            "raw": event
        }