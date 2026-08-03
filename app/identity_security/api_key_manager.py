import uuid
from datetime import datetime


class APIKeyManager:
    """
    Manages secure API access keys.
    """


    def create_key(
        self,
        service
    ):

        return {

            "service":
                service,

            "api_key":
                "sdna-" + uuid.uuid4().hex[:16],

            "status":
                "ACTIVE",

            "created_at":
                datetime.utcnow().isoformat()

        }