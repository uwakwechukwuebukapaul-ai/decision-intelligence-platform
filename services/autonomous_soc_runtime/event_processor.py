class EventProcessor:
    """
    Processes incoming security events.
    """

    def process(self, event):

        return {
            "event": event,
            "processed": True
        }


    def normalize(self, event):

        return {
            "normalized_event": event
        }