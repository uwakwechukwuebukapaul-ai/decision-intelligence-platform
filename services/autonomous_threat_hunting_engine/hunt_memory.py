class HuntMemory:

    def __init__(self):

        self.history = []


    def store(self, hunt):

        self.history.append(hunt)


    def retrieve(self):

        return self.history