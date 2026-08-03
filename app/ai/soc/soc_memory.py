from datetime import datetime
import uuid


class SOCMemory:


    def __init__(self):

        self.memory = []



    def store(
        self,
        investigation
    ):


        record = {

            "memory_id":
                "SOC-MEM-" +
                uuid.uuid4().hex[:8].upper(),

            "investigation":
                investigation,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.append(record)


        return record



    def get_history(self):


        return {

            "count":
                len(self.memory),

            "records":
                self.memory

        }