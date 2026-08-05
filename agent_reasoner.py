class AgentReasoner:

    def analyze(self, context):

        risk = "LOW"

        if context.get("severity") == "critical":
            risk = "HIGH"

        return {
            "decision": "investigate",
            "risk": risk,
            "reason": "Security context analyzed"
        }