from .integration_router import IntegrationRouter
from .investigation_orchestrator import InvestigationOrchestrator
from .core_logger import CoreLogger

from services.observability import ObservabilityManager

from services.intelligence_fusion import IntelligenceFusionEngine
from services.intelligence_memory import IntelligenceMemoryEngine
from services.decision_engine import DecisionEngine
from services.response_engine import ResponseEngine


class SentinelCorePipeline:
    """
    Autonomous Security Orchestrator.

    Full reasoning pipeline:

    Event
      |
    Intelligence Collection
      |
    Investigation
      |
    Fusion
      |
    Memory
      |
    Decision
      |
    Response
      |
    Observability
    """


    def __init__(self):

        self.router = IntegrationRouter()

        self.investigator = InvestigationOrchestrator()

        self.logger = CoreLogger()


        self.fusion = IntelligenceFusionEngine()

        self.memory = IntelligenceMemoryEngine()

        self.decision = DecisionEngine()

        self.response = ResponseEngine()


        self.observability = ObservabilityManager()


        self.observability.register_service(
            "sentinel_core"
        )


    def analyze(
        self,
        event
    ):

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


            fused_intelligence = self.fusion.fuse(

                event,

                evidence=investigation,

                detection=intelligence,

                threat={},

                cognitive={}

            )


            memory_record = self.memory.remember(
                event
            )


            decision = self.decision.decide(
                fused_intelligence
            )


            response = self.response.execute(
                decision
            )


            result = {

                "event":
                    event,


                "intelligence":
                    intelligence,


                "investigation":
                    investigation,


                "fusion":
                    fused_intelligence,


                "memory":
                    memory_record,


                "decision":
                    decision,


                "response":
                    response,


                # Backward compatibility
                "status":
                    "sentinel_pipeline_completed",


                # New autonomous pipeline metadata
                "pipeline_mode":
                    "autonomous_security_orchestration"

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