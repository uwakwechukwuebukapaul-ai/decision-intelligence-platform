from datetime import datetime


class WorkflowManager:

    def manage(self, incident):

        return {
            "workflow": [
                "Detection",
                "Analysis",
                "Containment",
                "Recovery"
            ],
            "incident": incident,
            "workflow_status": "active",
            "timestamp": datetime.utcnow().isoformat()
        }