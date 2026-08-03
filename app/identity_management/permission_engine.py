from datetime import datetime


class PermissionEngine:


    def get_permissions(self, role):

        permissions = {

            "Admin":
                [
                    "all_access"
                ],

            "SOC Analyst":
                [
                    "investigate",
                    "hunt",
                    "respond",
                    "report"
                ]

        }


        return {

            "role":
                role,

            "permissions":
                permissions.get(
                    role,
                    []
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }