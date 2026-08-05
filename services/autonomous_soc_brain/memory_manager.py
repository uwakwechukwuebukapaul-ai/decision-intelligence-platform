class MemoryManager:


    def __init__(self):

        self.history = []


    def store(self,event,decision):

        self.history.append(
            {
                "event":event,
                "decision":decision
            }
        )


    def recall(self):

        return self.history