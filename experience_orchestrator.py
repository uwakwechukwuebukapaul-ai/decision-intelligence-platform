class ExperienceOrchestrator:

    def __init__(self):
        self.workflows = []


    def launch_investigation_workspace(self, case_id):

        workflow = {
            "case_id": case_id,
            "workspace": "investigation",
            "status": "started"
        }

        self.workflows.append(workflow)

        return workflow


    def list_workflows(self):

        return self.workflows