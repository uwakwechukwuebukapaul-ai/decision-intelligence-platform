class SecurityOrchestrator:

    def __init__(self):
        self.workflows = []

    def create_workflow(self, name):
        workflow = {
            "name": name,
            "status": "created"
        }

        self.workflows.append(workflow)

        return workflow


    def execute(self, workflow):
        workflow["status"] = "executed"

        return workflow