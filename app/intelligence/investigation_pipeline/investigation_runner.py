"""
Sentinel DNA
Investigation Runner

Executes planned investigation tasks.
"""

from app.intelligence.runtime import IntelligenceJob


class InvestigationRunner:


    def __init__(
        self,
        executor,
    ):

        self.executor = executor



    def run(
        self,
        investigation,
        tasks,
    ):

        results = []


        for task in tasks:

            job = IntelligenceJob(

                capability=
                    task["capability"],

                payload={
                    "investigation_id":
                        investigation.investigation_id,

                    "evidence":
                        investigation.evidence,
                },

            )


            result = self.executor.execute(
                job
            )


            results.append(
                result
            )


        return results