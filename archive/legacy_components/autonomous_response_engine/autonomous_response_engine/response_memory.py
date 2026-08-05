class ResponseMemory:
    """
    Stores response history and outcomes.
    """

    def __init__(self):

        self.history = []


    def store(self, response):

        self.history.append(response)


    def retrieve(self):

        return self.history