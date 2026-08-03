from datetime import datetime
import uuid


class IdentityMemory:


    def store(self, username):

        return {

            "memory_id":
                "IAM-" +
                str(uuid.uuid4())[:8].upper(),

            "stored":
                [
                    "User identity",
                    "Role assignment",
                    "Access history"
                ],

            "user":
                username,

            "timestamp":
                datetime.utcnow().isoformat()

        }