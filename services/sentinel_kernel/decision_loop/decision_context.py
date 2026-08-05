class DecisionContext:
    """
    Shared context passed through Sentinel DNA reasoning pipeline.

    Stores intelligence required for autonomous decisions.
    """

    def __init__(
        self,
        event=None,
        intelligence=None,
        evidence=None,
        memory=None
    ):

        self.event = event or {}

        self.intelligence = intelligence or {}

        self.evidence = evidence or []

        self.memory = memory or {}

        self.analysis = {}

        self.decision = {}

    def update_analysis(self, analysis):

        self.analysis = analysis

    def update_decision(self, decision):

        self.decision = decision

    def snapshot(self):

        return {
            "event": self.event,
            "intelligence": self.intelligence,
            "evidence": self.evidence,
            "memory": self.memory,
            "analysis": self.analysis,
            "decision": self.decision
        }