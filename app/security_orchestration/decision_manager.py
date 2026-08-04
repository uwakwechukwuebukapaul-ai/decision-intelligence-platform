from datetime import datetime


class DecisionManager:

    def decide(self, event):

        critical_keywords = [
            "ransomware",
            "malware",
            "attack",
            "powershell",
            "breach"
        ]

        risk = "high"

        if any(word in event.lower() for word in critical_keywords):
            risk = "critical"

        return {
            "decision": "Immediate security response required"
            if risk == "critical"
            else "Continue investigation",

            "risk_level": risk,

            "reasoning": [
                "Threat behavior detected",
                "Security impact evaluated",
                "Response priority assigned"
            ],

            "timestamp": datetime.utcnow().isoformat()
        }