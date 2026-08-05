class InvestigationHistory:
    """
    Stores historical investigation records.

    Used by:
    - AI SOC Copilot
    - Threat Hunting Engine
    - Cognitive Memory
    - Analyst learning systems
    """

    def __init__(self):

        self.history = []


    def record(self, investigation):

        entry = {
            "id": len(self.history) + 1,
            "investigation": investigation
        }

        self.history.append(entry)

        return entry


    def get_all(self):

        return self.history


    def get_by_id(self, investigation_id):

        for item in self.history:

            if item["id"] == investigation_id:

                return item

        return None


    def count(self):

        return len(self.history)