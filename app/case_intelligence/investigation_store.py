from datetime import datetime


class InvestigationStore:
    """
    Stores investigation workflows.
    """

    def __init__(self):
        self.investigations = []


    def save(self, case_id, actions):

        investigation = {
            "case_id": case_id,
            "actions": actions,
            "status": "ACTIVE",
            "created_at": datetime.utcnow().isoformat()
        }

        self.investigations.append(investigation)

        return investigation


    def get(self, case_id):

        return [
            item for item in self.investigations
            if item["case_id"] == case_id
        ]