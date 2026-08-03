from datetime import datetime
import uuid


class HuntMemory:


    def store(self, event):

        return {

            "memory_id":
                "HUNT-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                event,

            "stored_patterns":

                [

                    "Behavior patterns",

                    "Attack techniques",

                    "Investigation results"

                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }