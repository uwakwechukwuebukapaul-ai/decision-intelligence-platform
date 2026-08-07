"""
Investigation API

Service interface for Sentinel DNA investigations.
"""


class InvestigationAPI:


    def __init__(
        self,
        orchestrator,
    ):

        self.orchestrator = orchestrator



    def create_investigation(
        self,
        case_id,
        execution_plan,
    ):

        report = self.orchestrator.investigate(

            case_id,

            execution_plan,

        )


        return {

            "status":
                "completed",

            "investigation":
                report,

        }