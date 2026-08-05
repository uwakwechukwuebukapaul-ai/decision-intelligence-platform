class SchemaMapper:
    """
    Maps external schemas into Sentinel DNA format.
    """

    def map(self, event):

        return {
            "security_event": {
                "source": event.get("source"),
                "type": event.get("type"),
                "data": event
            }
        }