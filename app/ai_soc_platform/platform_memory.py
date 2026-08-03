from datetime import datetime
import uuid


class PlatformMemory:


    def store(self, alert, investigation):

        return {

            "memory_id":

                "SOCMEM-" + str(uuid.uuid4())[:8].upper(),

            "incident": alert,

            "stored_patterns":

                investigation["steps"],

            "timestamp":

                datetime.utcnow().isoformat()

        }