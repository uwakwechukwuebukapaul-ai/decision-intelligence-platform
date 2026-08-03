from datetime import datetime


class DecisionReasoner:
    """
    Generates operational decisions.
    """

    def decide(self, risk):

        level = risk.get(
            "risk_level"
        )


        if level == "critical":

            decision = "IMMEDIATE_RESPONSE"


        elif level == "high":

            decision = "INVESTIGATE_AND_CONTAIN"


        elif level == "medium":

            decision = "MONITOR_ACTIVITY"


        else:

            decision = "NO_ACTION_REQUIRED"


        return {

            "decision":
                decision,

            "timestamp":
                datetime.utcnow().isoformat()

        }