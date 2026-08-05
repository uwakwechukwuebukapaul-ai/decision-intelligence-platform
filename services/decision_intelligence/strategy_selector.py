class StrategySelector:

    def __init__(self):
        self.strategies = [
            "investigate",
            "monitor",
            "respond",
            "escalate"
        ]


    def select(self, prediction, confidence):

        if confidence >= 0.8:
            return "respond"

        if prediction.get("risk") == "high":
            return "investigate"

        if prediction.get("risk") == "medium":
            return "monitor"

        return "observe"