"""
Sentinel DNA
Intelligence Coordinator

Coordinates investigation workflow execution.
"""


class Coordinator:

    def __init__(
        self,
        executor=None,
        pipeline=None,
        memory=None,
    ):

        self.executor = executor
        self.pipeline = pipeline
        self.memory = memory


    def execute(
        self,
        plan,
    ):
        """
        Execute an investigation plan.
        """

        if plan is None:

            return {

                "status": "failed",

                "error":
                    "Invalid investigation plan"

            }


        if hasattr(plan, "validate"):

            plan.validate()


        jobs = self._extract_jobs(
            plan
        )


        results = []


        for job in jobs:

            if self.executor is None:

                return {

                    "status":
                        "failed",

                    "error":
                        "Executor unavailable"

                }


            result = self.executor.execute(
                job
            )


            results.append(
                result
            )


        return {

            "status":
                "completed",

            "results":
                results,

            "job_count":
                len(results),

        }



    def execute_workflow(
        self,
        plan,
    ):

        return self.execute(
            plan
        )



    def _extract_jobs(
        self,
        plan,
    ):
        """
        Supports different investigation plan formats.
        """

        if hasattr(
            plan,
            "jobs"
        ):

            return plan.jobs


        if hasattr(
            plan,
            "steps"
        ):

            return plan.steps


        if isinstance(
            plan,
            list
        ):

            return plan


        return []



    def investigate(
        self,
        investigation,
    ):

        result = self.execute(
            investigation
        )


        if self.memory:

            self.memory.remember(
                investigation,
                result
            )


        return result



    def health(
        self,
    ):

        return {

            "component":
                "coordinator",

            "status":
                "ready",

            "executor":
                self.executor is not None,

            "pipeline":
                self.pipeline is not None,

            "memory":
                self.memory is not None,

        }