from datetime import datetime


class WorkflowEngine:

    def execute(self, incident):

        return {
            "incident": incident,
            "workflow": [
                "Detection received",
                "Incident classified",
                "Investigation started",
                "Response executed",
                "Audit recorded"
            ],
            "status": "completed",
            "timestamp": datetime.now().isoformat()
        }