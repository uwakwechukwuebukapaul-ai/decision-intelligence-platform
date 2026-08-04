import datetime
import uuid


class CognitiveMemory:
    """
    Stores cognitive investigation history.
    """

    def __init__(self):
        self.history = []


    def store(self, data):

        memory_id = (
            "COG-"
            + uuid.uuid4()
            .hex[:8]
            .upper()
        )

        record = {

            "memory_id": memory_id,

            "stored": [
                "Investigation Context",
                "Reasoning Results",
                "Security Decisions"
            ],

            "data": data,

            "timestamp":
                datetime.datetime.utcnow().isoformat()

        }

        self.history.append(record)

        return record