from datetime import datetime


class InvestigationMemory:

    def __init__(self):
        self.investigations = []

    def store_investigation(self, investigation):
        record = {
            "type": "investigation",
            "data": investigation,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.investigations.append(record)

        return record

    def retrieve_all(self):
        return self.investigations

    def search(self, keyword):
        results = []

        for item in self.investigations:
            if keyword.lower() in str(item).lower():
                results.append(item)

        return results