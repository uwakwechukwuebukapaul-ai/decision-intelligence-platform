class RiskController:
    def __init__(self):
        self.status = "ready"

    def evaluate(self, risk):
        return {
            "risk": risk,
            "decision": "controlled"
        }