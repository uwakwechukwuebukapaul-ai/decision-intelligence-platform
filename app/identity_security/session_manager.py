import uuid
from datetime import datetime


class SessionManager:
    """
    Enterprise session security.
    """


    def create_session(
        self,
        user
    ):

        return {

            "session_id":
                "SESSION-" + uuid.uuid4().hex[:8],

            "user":
                user,

            "status":
                "ACTIVE",

            "created_at":
                datetime.utcnow().isoformat()

        }


    def revoke_session(
        self,
        session_id
    ):

        return {

            "session_id":
                session_id,

            "status":
                "REVOKED",

            "timestamp":
                datetime.utcnow().isoformat()

        }