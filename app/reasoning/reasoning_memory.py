from datetime import datetime
import hashlib


class ReasoningMemory:

    def __init__(self):

        self.records = []


    def store(self, reasoning):

        identity = hashlib.sha256(
            str(reasoning).encode()
        ).hexdigest()


        record = {

            "reasoning_id":
                "REASON-" + identity[:8],

            "data":
                reasoning,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.records.append(record)

        return record


    def history(self):

        return {

            "count":
                len(self.records),

            "records":
                self.records

        }