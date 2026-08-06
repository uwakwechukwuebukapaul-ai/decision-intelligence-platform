class EvidenceRepository:


    def __init__(self):

        self.records=[]


    def save(self,data):

        self.records.append(data)

        return data


    def all(self):

        return self.records