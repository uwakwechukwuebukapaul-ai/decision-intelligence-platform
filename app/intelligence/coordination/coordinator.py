"""
Coordinator

Coordinates workflow execution
through the intelligence runtime.
"""

from app.intelligence.runtime.job import IntelligenceJob

from .result_aggregator import ResultAggregator


class Coordinator:
    """
    Executes intelligence workflows.
    """

    def __init__(
        self,
        executor,
    ):
        self.executor = executor


    def execute(
        self,
        execution_plan,
    ):

        execution_plan.validate()

        aggregator = ResultAggregator()


        for step in execution_plan.ordered_steps():

            job = IntelligenceJob(
                capability=step.capability,
                payload=step.payload,
            )


            execution_result = self.executor.execute(
                job
            )


            workflow_result = {

                "step": step.name,

                "capability": step.capability,

                "status": execution_result.get(
                    "status"
                ),

                "execution": execution_result,

            }


            aggregator.add_result(
                workflow_result
            )


        return aggregator.investigation_result()