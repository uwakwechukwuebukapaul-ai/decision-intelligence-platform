from datetime import datetime


class RiskMemory:

    def __init__(self):
        self.history = []

    def store(self, event, risk):

        self.history.append(
            {
                "event": event,
                "risk": risk,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return True

    def get_history(self):

        return self.history