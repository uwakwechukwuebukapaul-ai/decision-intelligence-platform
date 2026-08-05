class ThreatMemory:

    def __init__(self):
        self.threats = []

    def add_threat(self, threat):
        self.threats.append(threat)
        return threat

    def get_threats(self):
        return self.threats