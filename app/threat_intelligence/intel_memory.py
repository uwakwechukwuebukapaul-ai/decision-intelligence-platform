from datetime import datetime
import uuid


class IntelMemory:


    def store(self,event,data):

        return {

            "memory_id":

                "INTEL-" + str(uuid.uuid4())[:8],

            "event":

                event,

            "stored":

                [

                    "IOC Intelligence",

                    "Threat Actors",

                    "Malware Intelligence",

                    "Campaign Data"

                ],

            "timestamp":

                datetime.utcnow().isoformat()

        }