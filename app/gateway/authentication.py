from datetime import datetime
import uuid


class Authentication:

    """
    Enterprise authentication foundation.
    """


    def authenticate(self, user):

        token = (
            "SDNA-"
            +
            str(uuid.uuid4())
        )


        return {

            "user":
                user,

            "authenticated":
                True,

            "token":
                token,

            "timestamp":
                datetime.utcnow().isoformat()
        }