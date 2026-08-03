from datetime import datetime
import uuid


class IdentityLogger:


    def record(self, username):

        return {

            "log_id":
                "ID-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Identity authenticated",

            "user":
                username,

            "timestamp":
                datetime.utcnow().isoformat()

        }