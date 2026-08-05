class EventRepository:
    """
    Stores normalized security events.
    """

    def __init__(self):

        self.events = []


    def add_event(self, event):

        self.events.append(event)

        return {
            "stored": True,
            "event_id": len(self.events)
        }


    def get_events(self):

        return self.events