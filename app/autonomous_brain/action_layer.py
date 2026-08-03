from datetime import datetime


class ActionLayer:
    """
    Generates security response actions.
    """

    def execute(self, reasoning):

        decision = reasoning.get(
            "reasoning",
            ""
        )


        if "ransomware" in decision.lower():

            actions = [
                "Isolate affected systems",
                "Block malicious indicators",
                "Start incident response workflow",
                "Notify security leadership"
            ]

        else:

            actions = [
                "Continue monitoring",
                "Collect additional evidence"
            ]


        return {
            "actions": actions,
            "timestamp": datetime.utcnow().isoformat()
        }