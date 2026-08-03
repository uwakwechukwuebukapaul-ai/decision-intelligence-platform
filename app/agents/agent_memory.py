from datetime import datetime
import hashlib


class AgentMemory:

    def __init__(self):
        self.memory = []

    def store(self, agent, action, result):

        record = {
            "memory_id": "AGENT-" +
            hashlib.sha256(
                str(datetime.now()).encode()
            ).hexdigest()[:8].upper(),

            "agent": agent,
            "action": action,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(record)

        return record


    def history(self):

        return {
            "count": len(self.memory),
            "records": self.memory
        }