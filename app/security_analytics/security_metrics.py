from datetime import datetime


class SecurityMetrics:


    def calculate(self, event):

        return {

            "security_score":
                90
                if "ransomware" in event.lower()
                else 60,

            "metrics": [

                "Threat Detection",
                "Response Readiness",
                "Attack Visibility"

            ],

            "timestamp":
                datetime.utcnow().isoformat()

        }