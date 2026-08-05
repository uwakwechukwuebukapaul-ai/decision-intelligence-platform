class ResponseOrchestrator:

    def orchestrate(self, incident):

        return {
            "workflow": "incident_response",
            "incident": incident,
            "status": "running"
        }