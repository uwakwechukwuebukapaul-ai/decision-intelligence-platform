from datetime import datetime


class WorkflowEngine:


    def __init__(self):

        self.workflows = []



    def create_workflow(
        self,
        mission_id,
        agents
    ):

        workflow = {

            "workflow_id":
                f"WORKFLOW-{len(self.workflows)+1}",

            "mission_id":
                mission_id,

            "agents":
                agents,

            "status":
                "active",

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.workflows.append(
            workflow
        )


        return workflow



    def get_workflows(self):

        return self.workflows