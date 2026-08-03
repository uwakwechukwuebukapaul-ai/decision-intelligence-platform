from datetime import datetime
import uuid


class SessionManager:


    def create_session(self, username):

        return {

            "session_id":
                "SESSION-" +
                str(uuid.uuid4())[:8].upper(),

            "username":
                username,

            "status":
                "active",

            "created_at":
                datetime.utcnow().isoformat()

        }