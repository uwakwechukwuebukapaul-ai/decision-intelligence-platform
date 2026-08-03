from datetime import datetime


class ResponseReasoner:


    def recommend(self, decision):

        return {

            "response":

                decision["recommended_action"],

            "workflow":

                [
                    "Validate",
                    "Contain",
                    "Investigate",
                    "Recover"
                ],

            "timestamp":
                datetime.utcnow().isoformat()
        }