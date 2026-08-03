from datetime import datetime


class AttackPrediction:


    def predict(self, event):

        prediction = "Low probability"

        if "ransomware" in event.lower():

            prediction = (
                "Possible ransomware escalation "
                "and operational impact"
            )


        return {

            "prediction":
                prediction,

            "confidence":
                "high"
                if "ransomware" in event.lower()
                else "medium",

            "timestamp":
                datetime.utcnow().isoformat()

        }