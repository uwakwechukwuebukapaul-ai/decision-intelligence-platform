import uuid
from datetime import datetime


class Authentication:


    def authenticate(self, username):

        return {

            "authenticated":
                True,

            "user_id":
                "USER-"
                + uuid.uuid4().hex[:8].upper(),

            "username":
                username,

            "timestamp":
                datetime.utcnow().isoformat()
        }