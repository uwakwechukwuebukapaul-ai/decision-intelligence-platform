from datetime import datetime


class AIInsights:
    """
    AI generated analyst recommendations.
    """


    def generate(self, event):

        text = str(event).lower()


        recommendations = []


        if "ransomware" in text:

            recommendations = [

                "Isolate affected systems",

                "Block malicious indicators",

                "Investigate lateral movement",

                "Start incident response"

            ]


        else:

            recommendations = [

                "Review security evidence",

                "Investigate activity"

            ]


        return {

            "insights":
                recommendations,

            "confidence":
                95,

            "timestamp":
                datetime.utcnow().isoformat()

        }