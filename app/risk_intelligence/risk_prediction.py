from datetime import datetime


class RiskPrediction:

    def predict(self, event, risk):

        if risk["risk_score"] >= 80:
            prediction = (
                "High probability of business disruption. "
                "Immediate response recommended."
            )

        else:
            prediction = (
                "Risk currently manageable."
            )

        return {
            "prediction": prediction,
            "confidence": 90,
            "timestamp": datetime.utcnow().isoformat()
        }