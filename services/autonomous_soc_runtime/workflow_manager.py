class WorkflowManager:
    """
    Manages SOC workflows.
    """

    def create_workflow(self, name):

        return {
            "workflow": name,
            "status": "created"
        }


    def run(self, workflow):

        return {
            "workflow": workflow,
            "status": "running"
        }