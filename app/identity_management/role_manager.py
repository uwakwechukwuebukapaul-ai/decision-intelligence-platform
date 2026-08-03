from datetime import datetime


class RoleManager:


    def assign_role(self, username, role):

        return {

            "username":
                username,

            "role":
                role,

            "assigned_at":
                datetime.utcnow().isoformat()

        }