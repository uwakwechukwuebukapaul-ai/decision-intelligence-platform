class DecisionOrchestrator:
    """
    Converts intelligence output into security decisions.
    """

    def decide(self, intelligence):

        risk = intelligence.get(
            "risk",
            "unknown"
        )

        if risk == "critical":
            action = "immediate_response"

        elif risk == "high":
            action = "analyst_investigation"

        else:
            action = "monitor"


        return {
            "decision": action,
            "confidence": "high",
            "source": "sentinel_kernel"
        }