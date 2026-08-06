import uuid


class LearningRepository:

    def __init__(self):
        self.records = []

    def save(self, data):
        self.records.append(data)
        return data

    def generate_id(self):
        return f"LRN-{uuid.uuid4().hex[:8].upper()}"

    def get_all(self):
        return self.records