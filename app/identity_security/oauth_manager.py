import uuid
from datetime import datetime


class OAuthManager:
    """
    OAuth2 authorization manager.
    """


    def generate_token(
        self,
        client
    ):

        return {

            "client":
                client,

            "access_token":
                "oauth-" + uuid.uuid4().hex[:12],

            "expires":
                "1 hour",

            "timestamp":
                datetime.utcnow().isoformat()

        }