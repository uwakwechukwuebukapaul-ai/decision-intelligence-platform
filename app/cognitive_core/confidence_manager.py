from datetime import datetime


class ConfidenceManager:

    def evaluate(self, reasoning):

        factors = len(
            reasoning.get("reasoning", [])
        )

        if factors >= 3:
            confidence = "96%"

        elif factors == 2:
            confidence = "85%"

        else:
            confidence = "70%"


        return {
            "confidence": confidence,
            "factors_checked": factors,
            "timestamp": datetime.utcnow().isoformat()
        }