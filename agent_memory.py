class AgentMemory:

    def __init__(self):
        self.memory = []

    def store(self, event):
        self.memory.append(event)

    def recall(self):
        return self.memory

    def search(self, keyword):

        return [
            item for item in self.memory
            if keyword.lower() in str(item).lower()
        ]