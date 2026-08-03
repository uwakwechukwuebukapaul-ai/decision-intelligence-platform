from datetime import datetime
import uuid


class IntelMemory:


    def __init__(self):

        self.records = []


    def store(self, threat):

        record = {

            "memory_id":
            f"INTEL-{uuid.uuid4().hex[:8].upper()}",

            "threat": threat,

            "stored": [
                "IOC intelligence",
                "Threat actors",
                "Campaign history",
                "Malware intelligence"
            ],

            "timestamp":
            datetime.utcnow().isoformat()
        }


        self.records.append(record)

        return record