from app.intelligence.coordination.workflow import Workflow

from .workflow_context import WorkflowContext
from .workflow_result import WorkflowResult
from .workflow_state import WorkflowState


class WorkflowExecutor:
    """
    Executes workflow definitions.
    """


    def execute(
        self,
        workflow: Workflow,
        context: WorkflowContext,
    ):

        try:

            for step in workflow.steps:

                context.set_output(
                    step.name,
                    {
                        "capability":
                        step.capability,
                        "status":
                        "completed"
                    }
                )


            return WorkflowResult(
                workflow_id=context.workflow_id,
                state=WorkflowState.COMPLETED.value,
                data=context.outputs,
            )


        except Exception as error:

            return WorkflowResult(
                workflow_id=context.workflow_id,
                state=WorkflowState.FAILED.value,
                error=str(error),
            )