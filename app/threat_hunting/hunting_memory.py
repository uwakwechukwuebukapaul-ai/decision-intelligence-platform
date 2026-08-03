from datetime import datetime


class HuntingMemory:

    def __init__(self):
        self.history = []

    def store(self, threat):

        self.history.append(
            {
                "threat": threat,
                "timestamp":
                    datetime.utcnow().isoformat()
            }
        )

        return True

    def get_history(self):

        return self.history