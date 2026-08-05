class EventRepository:
    """
    Security event persistence layer.

    Stores normalized events from:
    - SIEM
    - EDR
    - Cloud logs
    - Network telemetry
    """

    def __init__(self):

        self.events = []


    def add_event(self, event):

        record = {
            "id": len(self.events) + 1,
            "event": event
        }

        self.events.append(record)

        return record


    def get_events(self):

        return self.events


    def count(self):

        return len(self.events)