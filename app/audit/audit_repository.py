class AuditRepository:

    def __init__(self):
        self.events = []


    def save(self, event):

        self.events.append(event)

        return event


    def get_by_incident(self, incident_id):

        return [
            event
            for event in self.events
            if event["incident_id"] == incident_id
        ]