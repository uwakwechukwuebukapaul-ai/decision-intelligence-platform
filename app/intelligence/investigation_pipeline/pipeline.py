"""
Sentinel DNA
Investigation Pipeline

Main investigation orchestration layer.
"""

from .pipeline_result import PipelineResult
from .task_planner import TaskPlanner
from .investigation_runner import InvestigationRunner



class InvestigationPipeline:


    def __init__(
        self,
        executor,
    ):

        self.executor = executor

        self.planner = TaskPlanner()

        self.runner = InvestigationRunner(
            executor
        )



    def execute(
        self,
        investigation,
    ):

        result = PipelineResult(
            investigation.investigation_id
        )


        try:

            tasks = self.planner.create_tasks(
                investigation
            )


            execution_results = (
                self.runner.run(
                    investigation,
                    tasks,
                )
            )


            for item in execution_results:

                result.add_result(
                    item
                )


            result.complete()


        except Exception as error:

            result.fail()

            result.add_result(
                {
                    "error":
                        str(error)
                }
            )


        return result.to_dict()