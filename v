class StrategySelector:

    def __init__(self):
        self.name = "Strategy Selector"

    def select(self, prediction, confidence):

        if confidence >= 0.8:
            return {
                "strategy": "automated_response",
                "reason": "high confidence decision"
            }

        return {
            "strategy": "analyst_review",
            "reason": "requires human validation"
        }