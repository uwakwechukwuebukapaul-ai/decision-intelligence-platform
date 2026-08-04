import uuid
import datetime


class IntelligenceMemory:
    """
    Stores autonomous investigation history.
    """


    def __init__(self):

        self.records = []


    def store(self, data):

        record = {

            "memory_id":
                "INTEL-"
                + uuid.uuid4()
                .hex[:8]
                .upper(),

            "data": data,

            "timestamp":
                datetime.datetime.now(datetime.timezone.utc).isoformat()

        }


        self.records.append(record)

        return record
