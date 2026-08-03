from datetime import datetime


class HypothesisEngine:


    def create(self, event):

        return {

            "hypothesis":

                "Adversary activity may be attempting "
                "unauthorized execution and impact",

            "confidence":
                "high",

            "timestamp":
                datetime.utcnow().isoformat()

        }