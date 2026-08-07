"""
Investigation Orchestrator

Coordinates complete SOC investigation flow.
"""


from app.intelligence.context import (
    load_investigation_context,
)



class InvestigationOrchestrator:

    def __init__(
        self,
        coordinator,
        reasoning_engine,
        report_generator,
    ):

        self.coordinator = coordinator

        self.reasoning_engine = reasoning_engine

        self.report_generator = report_generator



    def investigate(
        self,
        case_id,
        execution_plan,
    ):

        context = load_investigation_context(
            case_id
        )


        results = self.coordinator.execute(
            execution_plan
        )


        intelligence_results = results.get(
            "results",
            []
        )


        assessment = self.reasoning_engine.analyze(
            intelligence_results
        )


        report = self.report_generator.generate(

            case_id,

            assessment,

            intelligence_results,

        )


        return report