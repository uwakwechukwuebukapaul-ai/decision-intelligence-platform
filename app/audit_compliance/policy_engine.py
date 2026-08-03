class PolicyEngine:
    """
    Security authorization policy engine.
    """


    def __init__(self):

        self.policies = {


            "SOC_ANALYST": [

                "view_alerts",

                "investigate_cases",

                "view_reports"

            ],


            "SOC_MANAGER": [

                "manage_cases",

                "approve_response",

                "view_reports"

            ],


            "ADMIN": [

                "manage_users",

                "manage_policies",

                "view_audit"

            ]

        }



    def check(
        self,
        role,
        action
    ):

        return action in self.policies.get(
            role,
            []
        )



    def get_policy(
        self,
        role
    ):

        return {

            "role":
                role,

            "permissions":
                self.policies.get(
                    role,
                    []
                )

        }