class SecurityReasoningEngine:

    def reason(
        self,
        threat,
        behavior
    ):

        risk = "low"

        if threat.get("severity") == "high":
            risk = "high"

        return {
            "risk_level": risk,
            "assessment": "Security reasoning completed",
            "threat_context": threat,
            "behavior_context": behavior
        }