from datetime import datetime


class DataMemory:
    """
    Stores processed security data events.
    """


    def __init__(self):

        self.events = []


    def store(
        self,
        event
    ):

        record = {

            "event":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }

        self.events.append(record)

        return record


    def get_all(self):

        return {

            "events":
                self.events,

            "count":
                len(self.events)

        }