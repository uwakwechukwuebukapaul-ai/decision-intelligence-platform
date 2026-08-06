class IntelligenceRepository:

    def __init__(self):
        self.records = []


    def save(self, intelligence):

        self.records.append(intelligence)

        return intelligence


    def get_all(self):

        return self.records