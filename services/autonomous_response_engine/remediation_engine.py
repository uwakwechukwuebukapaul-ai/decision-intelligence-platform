class RemediationEngine:
    """
    Automated remediation capability.
    """

    def recommend(self, threat):

        return {
            "threat": threat,
            "remediation": [
                "isolate host",
                "block indicator",
                "reset credentials"
            ]
        }


    def apply(self, remediation):

        return {
            "status": "completed",
            "remediation": remediation
        }