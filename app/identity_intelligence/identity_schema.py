from datetime import datetime


class IdentitySchema:

    @staticmethod
    def create(
        username,
        role,
        department,
        privilege_level
    ):

        return {
            "username": username,
            "role": role,
            "department": department,
            "privilege_level": privilege_level,
            "created_at": datetime.utcnow().isoformat()
        }