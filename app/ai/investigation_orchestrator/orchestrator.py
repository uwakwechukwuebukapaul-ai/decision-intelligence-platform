"""
Sentinel DNA Investigation Orchestrator

Central AI SOC investigation controller.
"""


from .execution_pipeline import ExecutionPipeline



class InvestigationOrchestrator:


    def __init__(
        self,
        agent_registry
    ):

        self.pipeline = ExecutionPipeline(
            agent_registry
        )



    def investigate(
        self,
        investigation
    ):


        investigation.start()


        agents = [
            "EvidenceAgent"
        ]


        results = self.pipeline.execute(
            investigation,
            agents
        )


        investigation.complete()


        return {

            "investigation_id":
                investigation.investigation_id,

            "status":
                investigation.state.status.value,

            "results":
                results,

            "report":
                investigation.report()

        }