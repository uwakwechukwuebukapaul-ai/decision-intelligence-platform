"""
Sentinel DNA Investigation Orchestrator

Controls complete AI SOC investigations.
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

            "EvidenceAgent",

            "ThreatIntelligenceAgent",

            "MitreAgent",

            "RiskAgent",

            "ResponseAgent"

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

            "agents_executed":
                agents,

            "results":
                results,

            "report":
                investigation.report()

        }