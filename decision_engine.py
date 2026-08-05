class ResponseDecisionEngine:

    def evaluate(self, incident):

        severity = incident.get("severity", "medium") if isinstance(incident, dict) else "medium"

        return {
            "severity": severity,
            "decision": "execute_response",
            "confidence": 0.85
        }