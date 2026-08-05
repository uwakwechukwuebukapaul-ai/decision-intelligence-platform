class MemoryFusion:

    def __init__(self):

        self.memory = []


    def store(self, intelligence):

        self.memory.append(
            intelligence
        )


    def retrieve(self):

        return self.memory


    def latest(self):

        if self.memory:

            return self.memory[-1]

        return None