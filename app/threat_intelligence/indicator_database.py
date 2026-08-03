from datetime import datetime
import uuid


class IndicatorDatabase:


    def store(self, indicators):

        return {

            "database_id":
                "IOC-" +
                str(uuid.uuid4())[:8].upper(),

            "stored":
                True,

            "indicators":
                indicators,

            "timestamp":
                datetime.utcnow().isoformat()

        }