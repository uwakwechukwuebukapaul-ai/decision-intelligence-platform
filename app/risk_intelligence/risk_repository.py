import uuid


class RiskRepository:


    def __init__(self):

        self.records = []


    def generate_id(self):

        return f"RISK-{uuid.uuid4().hex[:8].upper()}"


    def save(self, record):

        self.records.append(record)

        return record


    def get_all(self):

        return self.records