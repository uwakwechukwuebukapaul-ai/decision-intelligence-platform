from datetime import datetime


class WorkflowOrchestrator:

    def create(self, incident, actions):

        return {
            "workflow": [
                "Detection",
                "Investigation",
                "Containment",
                "Response",
                "Recovery"
            ],
            "incident": incident,
            "actions": actions["actions"],
            "status": "ready_for_execution",
            "timestamp": datetime.utcnow().isoformat()
        }