from datetime import datetime
import uuid


class APILogger:


    def record(self, request_type):

        return {

            "log_id":

                "API-" + str(uuid.uuid4())[:8].upper(),

            "event":

                "API request processed",

            "request":

                request_type,

            "timestamp":

                datetime.utcnow().isoformat()

        }