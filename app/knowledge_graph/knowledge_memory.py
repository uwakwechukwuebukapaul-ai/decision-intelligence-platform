from datetime import datetime


class KnowledgeMemory:


    def __init__(self):

        self.history = []


    def store(
        self,
        knowledge
    ):

        self.history.append({

            "knowledge": knowledge,

            "timestamp":
                datetime.utcnow().isoformat()

        })

        return True


    def get_history(self):

        return self.history