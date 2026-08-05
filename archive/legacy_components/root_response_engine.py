class ResponseEngine:

    def execute(self, incident):
        return {
            "engine": "response",
            "status": "executed",
            "incident": incident
        }