from datetime import datetime


class DetectionMemory:

    def __init__(self):
        self.history = []

    def store(self, threat):

        event = {
            "threat": threat,
            "stored_at": datetime.utcnow().isoformat()
        }

        self.history.append(event)

        return event

    def get_history(self):

        return self.history