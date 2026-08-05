class WorkflowEngine:

    def __init__(self):

        self.workflows = [
            "alert_triage",
            "threat_enrichment",
            "investigation",
            "response"
        ]


    def start(self, event):

        return {
            "workflow": "security_investigation",
            "status": "started",
            "event": event
        }