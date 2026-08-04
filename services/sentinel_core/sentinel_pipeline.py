from .integration_router import IntegrationRouter
from .investigation_orchestrator import InvestigationOrchestrator
from .core_logger import CoreLogger


class SentinelCorePipeline:

    def __init__(self):

        self.router = IntegrationRouter()
        self.investigator = InvestigationOrchestrator()
        self.logger = CoreLogger()


    def analyze(self, event):

        intelligence = self.router.collect(event)

        investigation = self.investigator.process(
            event,
            intelligence
        )

        result = {
            "event": event,
            "intelligence": intelligence,
            "investigation": investigation,
            "status": "sentinel_pipeline_completed"
        }

        self.logger.log(result)

        return result