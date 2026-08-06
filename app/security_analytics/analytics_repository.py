import uuid


class AnalyticsRepository:


    def __init__(self):

        self.metrics = []


    def generate_id(self):

        return f"MET-{uuid.uuid4().hex[:8].upper()}"


    def save(self, metric):

        self.metrics.append(metric)

        return metric


    def get_all(self):

        return self.metrics