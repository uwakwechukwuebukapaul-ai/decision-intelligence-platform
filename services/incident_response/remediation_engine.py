class RemediationEngine:

    def execute(self, actions):

        remediation = []

        for action in actions:

            remediation.append(
                {
                    "action": action,
                    "result": "remediation_planned"
                }
            )

        return remediation