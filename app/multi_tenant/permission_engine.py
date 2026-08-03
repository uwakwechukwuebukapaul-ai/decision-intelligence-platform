class PermissionEngine:
    """
    Controls RBAC permissions.
    """


    def __init__(self):

        self.permissions = {


            "SUPER_ADMIN": [

                "manage_tenants",

                "manage_users",

                "execute_response",

                "view_reports"

            ],


            "SOC_MANAGER": [

                "view_alerts",

                "manage_cases",

                "view_reports"

            ],


            "SECURITY_ANALYST": [

                "view_alerts",

                "investigate_cases"

            ],


            "THREAT_HUNTER": [

                "hunt_threats",

                "view_intelligence"

            ],


            "VIEW_ONLY": [

                "view_dashboard"

            ]

        }



    def get_permissions(self, role):

        return {

            "role":
                role,

            "permissions":
                self.permissions.get(
                    role,
                    []
                )

        }



    def check_permission(
        self,
        role,
        permission
    ):

        return permission in self.permissions.get(
            role,
            []
        )