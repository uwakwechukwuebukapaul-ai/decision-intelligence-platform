from datetime import datetime


class DecisionTracker:


    def track(self, decision):

        return {

            "decision":
                decision,

            "tracked":
                True,

            "timestamp":
                datetime.utcnow().isoformat()
        }