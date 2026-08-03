class RoleManager:
    """
    Enterprise RBAC role definitions.
    """


    def __init__(self):

        self.roles = [

            "SUPER_ADMIN",

            "SOC_MANAGER",

            "SECURITY_ANALYST",

            "THREAT_HUNTER",

            "VIEW_ONLY"

        ]


    def list_roles(self):

        return {

            "roles":
                self.roles,

            "count":
                len(self.roles)

        }


    def validate(self, role):

        return role in self.roles