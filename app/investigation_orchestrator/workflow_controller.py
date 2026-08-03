from datetime import datetime


class WorkflowController:


    def control(self, event):

        return {

            "workflow":

            [

                "Detection",
                "Investigation",
                "Decision",
                "Response"

            ],

            "event":
                event,

            "workflow_status":
                "active",

            "timestamp":
                datetime.utcnow().isoformat()
        }