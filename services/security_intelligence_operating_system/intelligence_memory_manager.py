class IntelligenceMemoryManager:

    def __init__(self):

        self.memory = []


    def store(self, data):

        self.memory.append(data)


    def retrieve(self):

        return self.memory