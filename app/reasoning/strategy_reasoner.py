from datetime import datetime


class StrategyReasoner:
    """
    Creates recommended response strategies.
    """

    def recommend(self, decision):

        action = decision["decision"]


        strategies = {

            "IMMEDIATE_RESPONSE":
                [
                    "Isolate affected systems",
                    "Start incident response workflow",
                    "Notify security leadership"
                ],

            "INVESTIGATE_AND_CONTAIN":
                [
                    "Collect additional evidence",
                    "Perform threat hunting",
                    "Prepare containment"
                ],

            "MONITOR_ACTIVITY":
                [
                    "Increase monitoring",
                    "Review security events"
                ],

            "NO_ACTION_REQUIRED":
                [
                    "Continue normal operations"
                ]
        }


        return {

            "strategy":
                strategies.get(
                    action,
                    []
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }