from datetime import datetime


class EventProcessor:

    def process(self, event):

        return {
            "event": event,
            "normalized_event": event.lower(),
            "processing_status": "normalized",
            "timestamp": datetime.utcnow().isoformat()
        }