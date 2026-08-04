from services.investigation_runtime import InvestigationRuntimeEngine
from services.incident_response import IncidentResponseEngine


class InvestigationOrchestrator:

    def __init__(self):

        self.runtime = InvestigationRuntimeEngine()
        self.response = IncidentResponseEngine()


    def process(self, event, intelligence):

        runtime_result = self.runtime.execute(
            event
        )

        response_result = self.response.respond(
            event
        )

        return {

            "runtime":
                runtime_result,

            "response":
                response_result,

            "status":
                "investigation_completed"

        }