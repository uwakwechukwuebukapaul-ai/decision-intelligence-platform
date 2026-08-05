class AgentMemory:
    """
    Memory layer for autonomous agents.
    """

    def __init__(self):
        self.memory = []

    def store(self, event):

        self.memory.append(event)

        return {
            "stored": True,
            "event": event
        }

    def retrieve(self):

        return self.memory