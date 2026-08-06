class AttackRepository:


    def __init__(self):

        self.paths = []



    def save(self, path):

        self.paths.append(path)

        return path



    def get_all(self):

        return self.paths