import uuid
import datetime


class FusedMemory:
    """
    Stores fused investigation intelligence.
    """

    def __init__(self):

        self.records = []


    def store(self, data):

        record = {

            "memory_id":
                "FUSION-"
                + uuid.uuid4()
                .hex[:8]
                .upper(),

            "data":
                data,

            "timestamp":
                datetime.datetime.now(
                    datetime.UTC
                ).isoformat()

        }


        self.records.append(record)


        return record