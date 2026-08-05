class ResponsePlanner:
    def __init__(self):
        self.status = "ready"

    def create_plan(self, incident):
        return {
            "plan": [
                "analyze",
                "contain",
                "remediate",
                "recover"
            ],
            "incident": incident
        }