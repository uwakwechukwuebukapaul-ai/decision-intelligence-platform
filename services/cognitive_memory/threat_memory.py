from datetime import datetime


class ThreatMemory:

    def __init__(self):
        self.threats = []

    def store_threat(self, threat):
        record = {
            "type": "threat",
            "data": threat,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.threats.append(record)

        return record

    def retrieve_threats(self):
        return self.threats

    def find_related(self, indicator):
        matches = []

        for threat in self.threats:
            if indicator.lower() in str(threat).lower():
                matches.append(threat)

        return matches