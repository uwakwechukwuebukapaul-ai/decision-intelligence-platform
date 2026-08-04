from datetime import datetime


class DecisionEngine:

    def decide(self, analysis, confidence):

        risk = analysis.get(
            "risk_level",
            "unknown"
        )

        confidence_score = confidence.get(
            "confidence",
            "0%"
        )


        if risk == "critical":

            decision = (
                "Immediate containment required"
            )

            priority = "critical"


        elif risk == "high":

            decision = (
                "Urgent investigation required"
            )

            priority = "high"


        else:

            decision = (
                "Continue monitoring"
            )

            priority = "medium"


        return {

            "decision": decision,

            "priority": priority,

            "risk_level": risk,

            "confidence": confidence_score,

            "timestamp":
                datetime.utcnow().isoformat()
        }