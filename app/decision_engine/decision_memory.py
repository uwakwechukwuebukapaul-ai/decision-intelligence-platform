from datetime import datetime
import uuid


class DecisionMemory:


    def store(self, incident, reasoning):

        return {

            "memory_id": "DEC-" + str(uuid.uuid4())[:8].upper(),

            "incident": incident,

            "learned_pattern": reasoning["analysis"],

            "timestamp": datetime.utcnow().isoformat()

        }