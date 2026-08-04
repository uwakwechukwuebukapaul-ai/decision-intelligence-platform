from .integration_router import IntegrationRouter
from .investigation_orchestrator import InvestigationOrchestrator
from .core_logger import CoreLogger

from services.observability import ObservabilityManager


class SentinelCorePipeline:

    def __init__(self):

        self.router = IntegrationRouter()
        self.investigator = InvestigationOrchestrator()
        self.logger = CoreLogger()

        self.observability = ObservabilityManager()

        self.observability.register_service(
            "sentinel_core"
        )


    def analyze(self, event):

        self.observability.start_execution(
            "sentinel_core"
        )

        try:

            intelligence = self.router.collect(
                event
            )

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


            self.observability.complete_execution(
                "sentinel_core",
                True
            )


            result["observability"] = (
                self.observability.report()
            )


            self.logger.log(
                result
            )


            return result


        except Exception:

            self.observability.complete_execution(
                "sentinel_core",
                False
            )

            raise