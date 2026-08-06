"""
Workflow Generator

Converts investigation strategies
into executable workflows.
"""

from app.intelligence.coordination.workflow import (
    Workflow,
    WorkflowStep,
)


class WorkflowGenerator:
    """
    Generates runtime workflows.
    """


    def generate(
        self,
        strategy,
    ) -> Workflow:


        workflow = Workflow(
            name="Autonomous Investigation",
            description=strategy.objective,
        )


        previous_step = None


        for index, capability in enumerate(
            strategy.capabilities
        ):

            step_name = (
                f"Step {index + 1}: {capability}"
            )


            step = WorkflowStep(
                name=step_name,
                capability=capability,
            )


            if previous_step:

                step.depends_on.append(
                    previous_step
                )


            workflow.add_step(
                step
            )


            previous_step = step_name


        return workflow