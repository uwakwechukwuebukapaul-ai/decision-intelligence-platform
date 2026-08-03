from datetime import datetime


class AuditLogger:
    """
    Tracks enterprise gateway activities.
    """


    def __init__(self):

        self.logs = []


    def log(self, action):

        entry = {

            "action":
                action,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.logs.append(entry)

        return entry



    def history(self):

        return self.logs