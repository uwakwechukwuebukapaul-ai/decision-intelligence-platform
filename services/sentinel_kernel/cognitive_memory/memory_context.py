class MemoryContext:
    """
    Represents stored Sentinel DNA experience.

    Keeps history required for learning.
    """

    def __init__(
        self,
        investigation_id=None,
        event=None,
        decision=None,
        outcome=None
    ):

        self.investigation_id = investigation_id

        self.event = event or {}

        self.decision = decision or {}

        self.outcome = outcome or {}

        self.patterns = []

        self.learning = {}


    def add_pattern(
        self,
        pattern
    ):

        self.patterns.append(
            pattern
        )


    def update_learning(
        self,
        learning
    ):

        self.learning = learning


    def snapshot(self):

        return {

            "investigation_id":
                self.investigation_id,

            "event":
                self.event,

            "decision":
                self.decision,

            "outcome":
                self.outcome,

            "patterns":
                self.patterns,

            "learning":
                self.learning
        }