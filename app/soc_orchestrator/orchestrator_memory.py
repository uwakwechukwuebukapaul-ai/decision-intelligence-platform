class OrchestratorMemory:

    def __init__(self):
        self.history = []

    def store(self, incident):

        self.history.append(
            incident
        )

    def get_history(self):

        return self.history