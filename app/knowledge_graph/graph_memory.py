from datetime import datetime
import uuid


class GraphMemory:


    def store(self,event,relationships):

        return {

            "memory_id":
                f"GRAPH-{uuid.uuid4().hex[:8].upper()}",

            "event":
                event,

            "stored":[

                "Entities",

                "Relationships",

                "Attack Graph",

                "Threat Intelligence"

            ],

            "relationships":
                relationships,

            "timestamp":
                datetime.utcnow().isoformat()

        }