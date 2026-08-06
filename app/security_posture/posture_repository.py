class PostureRepository:

    def __init__(self):
        self.records = []

    def save(self, record):
        self.records.append(record)
        return record

    def all(self):
        return self.records