from datetime import datetime


class RiskVisualizer:
    """
    Converts security signals into dashboard risk metrics.
    """


    def calculate(self, event):

        text = str(event).lower()


        score = 20


        if "ransomware" in text:
            score += 70


        if "finance" in text:
            score += 10


        if score >= 80:
            level = "critical"

        elif score >= 60:
            level = "high"

        else:
            level = "medium"



        return {

            "risk_score":
                min(score,100),

            "risk_level":
                level,

            "timestamp":
                datetime.utcnow().isoformat()

        }