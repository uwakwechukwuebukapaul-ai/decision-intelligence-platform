class ResponsePlanner:

    def plan(self, incident):

        return {
            "plan": [
                "analyze",
                "contain",
                "remediate"
            ],
            "incident": incident
        }