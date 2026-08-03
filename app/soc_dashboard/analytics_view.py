from datetime import datetime


class AnalyticsView:


    def generate(self, incident):

        return {

            "metrics":

            [

                "Threat Detection",
                "Response Readiness",
                "Attack Visibility"

            ],

            "security_score":

                90,

            "timestamp":

                datetime.utcnow().isoformat()
        }