from datetime import datetime


class WorkflowManager:


    def execute(self, alert, copilot):

        return {

            "workflow":

            [

                "Detection",

                "Investigation",

                "Decision",

                "Response",

                "Learning"

            ],

            "actions":

            copilot["recommendations"],

            "status": "ready_for_execution",

            "timestamp": datetime.utcnow().isoformat()

        }