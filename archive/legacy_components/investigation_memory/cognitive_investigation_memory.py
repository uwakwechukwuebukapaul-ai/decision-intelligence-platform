class InvestigationMemory:


    def __init__(self):

        self.memory = []


    def store(self, investigation):

        self.memory.append(
            investigation
        )


    def retrieve(self):

        return self.memory


    def latest(self):

        if self.memory:

            return self.memory[-1]

        return None