from datetime import datetime


class CaseMemory:
    """
    AI memory for previous investigations.
    """


    def __init__(self):

        self.memory = []


    def remember(self, case_id, intelligence):

        record = {
            "case_id": case_id,
            "intelligence": intelligence,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.memory.append(record)

        return record


    def recall(self, keyword):

        return [
            item for item in self.memory
            if keyword.lower()
            in str(item["intelligence"]).lower()
        ]