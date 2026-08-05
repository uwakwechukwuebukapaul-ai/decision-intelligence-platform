class InvestigationEngine:
    """
    Core investigation lifecycle manager.
    """

    def __init__(self):
        self.status = "ready"

    def start(self, alert):
        return {
            "investigation_id": alert.get(
                "id",
                "INV-AUTO"
            ),
            "status": "started",
            "alert": alert
        }

    def complete(self, investigation):
        investigation["status"] = "completed"
        return investigation