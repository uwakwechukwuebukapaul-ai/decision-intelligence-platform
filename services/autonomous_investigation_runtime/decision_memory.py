class DecisionMemory:
    """
    Stores investigation decisions.

    Future:
    - vector database
    - embeddings
    - analyst feedback
    """


    def __init__(self):

        self.memory = []



    def remember(
        self,
        decision
    ):

        self.memory.append(decision)



    def recall(
        self
    ):

        return self.memory