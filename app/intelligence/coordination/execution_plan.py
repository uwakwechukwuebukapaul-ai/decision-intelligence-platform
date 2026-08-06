"""
Execution Plan

Transforms a workflow into an
ordered execution plan.
"""

from .workflow import Workflow, WorkflowStep


class ExecutionPlan:
    """
    Ordered execution plan.
    """

    def __init__(
        self,
        workflow: Workflow,
    ):

        self.workflow = workflow

    def validate(self) -> bool:
        """
        Validate workflow integrity.
        """

        names = self.workflow.step_names()

        for step in self.workflow.steps:

            for dependency in step.depends_on:

                if dependency not in names:
                    raise ValueError(
                        f"Unknown dependency: {dependency}"
                    )

        return True

    def ordered_steps(
        self,
    ) -> list[WorkflowStep]:
        """
        Current implementation returns
        workflow order.

        Future versions will support
        dependency resolution,
        parallel execution,
        priorities,
        and optimization.
        """

        self.validate()

        return list(self.workflow.steps)

    def summary(self) -> dict:

        return {
            "workflow": self.workflow.name,
            "step_count": self.workflow.step_count(),
            "valid": self.validate(),
        }