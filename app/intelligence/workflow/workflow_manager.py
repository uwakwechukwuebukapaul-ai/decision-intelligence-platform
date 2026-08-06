from .workflow_context import WorkflowContext
from .workflow_executor import WorkflowExecutor
from .workflow_registry import WorkflowRegistry


class WorkflowManager:
    """
    High level workflow controller.
    """


    def __init__(self):

        self.registry = WorkflowRegistry()
        self.executor = WorkflowExecutor()



    def register(
        self,
        workflow,
    ):

        self.registry.register(
            workflow
        )



    def run(
        self,
        workflow_name: str,
        workflow_id: str,
        inputs=None,
    ):

        workflow = self.registry.get(
            workflow_name
        )


        if workflow is None:

            raise ValueError(
                "Workflow not found"
            )


        context = WorkflowContext(
            workflow_id=workflow_id,
            inputs=inputs or {},
        )


        return self.executor.execute(
            workflow,
            context,
        )