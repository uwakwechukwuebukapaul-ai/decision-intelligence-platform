class InvestigationHistory:
    """
    Maintains investigation timelines.
    """

    def __init__(self):

        self.history = []


    def record(self, investigation):

        self.history.append(investigation)

        return {
            "recorded": True,
            "total": len(self.history)
        }


    def get_history(self):

        return self.history