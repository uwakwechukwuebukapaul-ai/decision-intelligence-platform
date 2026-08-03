from datetime import datetime
import uuid


class WorkspaceMemory:


    def store(self, incident):

        return {

            "memory_id":

                "WORK-" + str(uuid.uuid4())[:8].upper(),

            "incident":

                incident,

            "stored":

                [

                    "Analyst interaction",

                    "Investigation context",

                    "Dashboard state"

                ],

            "timestamp":

                datetime.utcnow().isoformat()

        }