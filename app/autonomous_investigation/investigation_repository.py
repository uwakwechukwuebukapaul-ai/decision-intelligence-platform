class InvestigationRepository:


    def __init__(self):

        self.records = []



    def save(self, investigation):

        self.records.append(investigation)

        return investigation



    def all(self):

        return self.records