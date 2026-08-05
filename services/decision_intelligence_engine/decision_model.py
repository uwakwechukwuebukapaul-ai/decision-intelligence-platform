class DecisionModel:
    def __init__(
        self,
        decision_type="investigation",
        confidence=0.0,
        priority="medium",
        actions=None
    ):
        self.decision_type = decision_type
        self.confidence = confidence
        self.priority = priority
        self.actions = actions or []

    def to_dict(self):
        return {
            "decision_type": self.decision_type,
            "confidence": self.confidence,
            "priority": self.priority,
            "actions": self.actions
        }