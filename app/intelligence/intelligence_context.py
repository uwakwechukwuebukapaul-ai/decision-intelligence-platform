class IntelligenceContext:
    """
    Shared context passed between intelligence components.
    """

    def __init__(
        self,
        user_id,
        objective=None,
        metadata=None
    ):
        self.user_id = user_id
        self.objective = objective
        self.metadata = metadata or {}

        self.decisions = []
        self.agent_actions = []
        self.feedback = []
        self.history = []


    def add_decision(self, decision):
        self.decisions.append(decision)


    def add_action(self, action):
        self.agent_actions.append(action)


    def add_feedback(self, feedback):
        self.feedback.append(feedback)


    def add_history(self, event):
        self.history.append(event)


    def to_dict(self):

        return {
            "user_id": self.user_id,
            "objective": self.objective,
            "metadata": self.metadata,
            "decisions": self.decisions,
            "agent_actions": self.agent_actions,
            "feedback": self.feedback,
            "history": self.history
        }