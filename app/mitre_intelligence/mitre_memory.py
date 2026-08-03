class MITREMemory:


    def __init__(self):

        self.history = []


    def store(self, data):

        self.history.append(data)


    def get_history(self):

        return self.history