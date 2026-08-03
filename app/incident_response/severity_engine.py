from datetime import datetime


class SeverityEngine:



    def calculate(self, alert):


        text = str(alert).lower()


        level = "medium"


        if any(
            item in text
            for item in [
                "ransomware",
                "critical",
                "data breach"
            ]
        ):

            level="critical"



        return {

            "level": level,

            "score":

                95 if level=="critical" else 50,

            "timestamp":
                datetime.utcnow().isoformat()

        }