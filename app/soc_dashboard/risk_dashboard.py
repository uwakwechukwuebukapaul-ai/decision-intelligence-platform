from datetime import datetime


class RiskDashboard:


    def calculate(self, incident):

        score = 100 if "ransomware" in incident.lower() else 50


        return {

            "risk_score":

                score,

            "risk_level":

                "critical"
                if score >= 80
                else "medium",

            "timestamp":

                datetime.utcnow().isoformat()
        }