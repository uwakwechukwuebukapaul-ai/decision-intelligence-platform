from datetime import datetime


class IntelMemory:
    """
    Stores intelligence records.
    """


    def __init__(self):

        self.records = []


    def store(
        self,
        record
    ):

        entry = {

            "record":
                record,

            "timestamp":
                datetime.utcnow().isoformat()

        }

        self.records.append(entry)

        return entry


    def get_history(self):

        return {

            "records":
                self.records,

            "count":
                len(self.records)

        }