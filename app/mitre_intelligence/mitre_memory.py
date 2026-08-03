import uuid
from datetime import datetime


class MITREMemory:


    def store(self, event):

        return {

            "memory_id":

                "MITRE-"
                + uuid.uuid4().hex[:8].upper(),


            "event":

                event,


            "stored":

            [

                "Techniques",
                "Tactics",
                "Attack Chains",
                "Detection Coverage"

            ],


            "timestamp":

                datetime.utcnow().isoformat()

        }