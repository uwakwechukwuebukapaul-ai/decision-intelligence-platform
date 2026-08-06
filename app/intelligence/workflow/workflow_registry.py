from typing import Dict

from app.intelligence.coordination.workflow import Workflow


class WorkflowRegistry:
    """
    Stores available workflow definitions.
    """


    def __init__(self):

        self._workflows: Dict[str, Workflow] = {}


    def register(
        self,
        workflow: Workflow,
    ):

        self._workflows[
            workflow.name
        ] = workflow



    def get(
        self,
        name: str,
    ):

        return self._workflows.get(name)



    def list(self):

        return list(
            self._workflows.keys()
        )