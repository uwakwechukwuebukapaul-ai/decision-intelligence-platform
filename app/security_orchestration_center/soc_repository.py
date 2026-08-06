class SOCRepository:

    def __init__(self):
        self.records = []

    def save(self, record):
        self.records.append(record)
        return record

    def get_all(self):
        return self.records

    def get_by_incident(self, incident_id):

        for record in self.records:
            if record["incident_id"] == incident_id:
                return record

        return None