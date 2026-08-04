from datetime import datetime
import uuid


class OrchestratorMemory:


    def store(self,event,decision):

        return {


            "memory_id":
                "ORCH-" + uuid.uuid4().hex[:8].upper(),


            "event":
                event,


            "stored":[

                "Investigation History",

                "Engine Coordination",

                "Security Decisions"

            ],


            "decision":
                decision,


            "timestamp":
                datetime.utcnow().isoformat()

        }