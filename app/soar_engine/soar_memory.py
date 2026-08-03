from datetime import datetime
import uuid


class SOARMemory:


    def store(self, incident, actions=None):

        return {

            "memory_id":
                "SOAR-" + uuid.uuid4().hex[:8].upper(),

            "incident":
                incident,

            "stored":
                [
                    "Playbook execution",
                    "Response actions",
                    "Workflow history",
                    "Automation decisions"
                ],

            "actions":
                actions if actions else [
                    "Containment workflow initiated"
                ],

            "timestamp":
                datetime.utcnow().isoformat()
        }