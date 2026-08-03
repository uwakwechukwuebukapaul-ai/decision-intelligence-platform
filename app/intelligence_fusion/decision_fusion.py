from datetime import datetime


class DecisionFusion:
    """
    Generates unified security decisions.
    """

    def decide(self, risk):

        level = risk.get("risk_level")


        if level == "critical":

            decision = (
                "Immediate containment, "
                "investigation and response required"
            )

        elif level == "high":

            decision = (
                "Prioritize investigation and "
                "prepare containment actions"
            )

        else:

            decision = (
                "Continue monitoring and analysis"
            )


        return {
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        }