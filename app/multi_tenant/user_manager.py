from datetime import datetime
import uuid


class UserManager:
    """
    Tenant user lifecycle management.
    """


    def create_user(
        self,
        name,
        email,
        role
    ):

        return {

            "user_id":
                "USR-" + uuid.uuid4().hex[:8].upper(),

            "name":
                name,

            "email":
                email,

            "role":
                role,

            "status":
                "ACTIVE",

            "created_at":
                datetime.utcnow().isoformat()

        }