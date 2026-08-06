import uuid


class DecisionRepository:


    def __init__(self):

        self.decisions = []


    def generate_id(self):

        return f"DEC-{uuid.uuid4().hex[:8].upper()}"


    def save(self, decision):

        self.decisions.append(decision)

        return decision


    def get_all(self):

        return self.decisions