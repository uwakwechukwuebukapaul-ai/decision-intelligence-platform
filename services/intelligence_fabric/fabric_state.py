class FabricState:


    def __init__(self):

        self.status = "initialized"


    def update(self, status):

        self.status = status


    def get(self):

        return self.status