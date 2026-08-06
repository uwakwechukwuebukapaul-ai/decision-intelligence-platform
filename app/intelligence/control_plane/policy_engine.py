"""
Policy Engine

Controls autonomous execution permissions.
"""


class PolicyEngine:


    def __init__(self):

        self.policies = {

            "allowed_capabilities": []

        }



    def allow_capability(
        self,
        capability: str,
    ):

        self.policies[
            "allowed_capabilities"
        ].append(
            capability
        )



    def check(
        self,
        capability: str,
    ) -> bool:


        return (
            capability
            in self.policies[
                "allowed_capabilities"
            ]
        )