from datetime import datetime


class ReasoningEngine:

    def analyze(self, context):

        reasoning = []

        event = context.get("event", "").lower()

        if "ransomware" in event:
            reasoning.append(
                "Ransomware behavior identified"
            )

        if "powershell" in event:
            reasoning.append(
                "Command execution behavior detected"
            )

        if "database" in event or "server" in event:
            reasoning.append(
                "Enterprise critical asset targeting detected"
            )

        risk = self.calculate_risk(reasoning)

        return {
            "reasoning": reasoning,
            "risk_level": risk,
            "analysis_status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        }


    def calculate_risk(self, reasoning):

        if len(reasoning) >= 3:
            return "critical"

        if len(reasoning) == 2:
            return "high"

        return "medium"