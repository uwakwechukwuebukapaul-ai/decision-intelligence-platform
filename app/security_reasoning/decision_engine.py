from datetime import datetime


class DecisionEngine:


    def decide(self, risk, threat):

        if risk["risk_level"] == "critical":

            decision = "Immediate containment required"

            action = "Execute SOAR containment workflow"

        else:

            decision = "Continue investigation"

            action = "Monitor activity"


        return {

            "decision": decision,

            "recommended_action": action,

            "confidence": "high",

            "timestamp":
                datetime.utcnow().isoformat()
        }