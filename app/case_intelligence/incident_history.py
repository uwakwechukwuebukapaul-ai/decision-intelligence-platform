from datetime import datetime


class IncidentHistory:

    """
    Maintains historical incident intelligence.
    """

    def __init__(self):
        self.history = []


    def record(self, case_id, event):

        entry = {
            "case_id": case_id,
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append(entry)

        return entry


    def timeline(self, case_id):

        return [
            event for event in self.history
            if event["case_id"] == case_id
        ]