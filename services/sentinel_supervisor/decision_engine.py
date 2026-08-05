class DecisionEngine:
    """
    Determines investigation strategy based on incident context.
    """

    def evaluate(self, incident):

        text = incident.lower()

        priority = "LOW"

        if any(
            keyword in text
            for keyword in [
                "ransomware",
                "breach",
                "malware",
                "credential",
            ]
        ):
            priority = "HIGH"

        if "critical" in text:
            priority = "CRITICAL"

        return {
            "priority": priority,
            "decision": "autonomous_investigation_required"
            if priority in ["HIGH", "CRITICAL"]
            else "monitor",
        }