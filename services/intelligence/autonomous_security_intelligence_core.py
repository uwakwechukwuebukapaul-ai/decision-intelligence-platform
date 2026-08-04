import datetime

from .engine_registry import IntelligenceEngineRegistry
from .investigation_pipeline import InvestigationPipeline
from .intelligence_memory import IntelligenceMemory
from .intelligence_logger import IntelligenceLogger


class AutonomousSecurityIntelligenceCore:
    """
    Sentinel DNA Autonomous Security Intelligence Core.

    Coordinates security intelligence engines
    into a unified investigation workflow.
    """


    def __init__(self):

        self.registry = IntelligenceEngineRegistry()

        self.pipeline = InvestigationPipeline()

        self.memory = IntelligenceMemory()

        self.logger = IntelligenceLogger()



    def register_engine(self, name, engine):

        self.registry.register(
            name,
            engine
        )



    def investigate(self, event):


        pipeline_result = self.pipeline.execute(
            event
        )


        memory = self.memory.store(
            {
                "event": event,
                "pipeline": pipeline_result
            }
        )


        log = self.logger.log(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "engine_status":
                self.registry.status(),

            "investigation":
                pipeline_result,

            "decision": {

                "risk_level":
                    "critical"
                    if "ransomware" in event.lower()
                    else "unknown",

                "confidence":
                    "96%"

            },


            "memory": memory,

            "log": log,


            "created_at":
                datetime.datetime.now(datetime.timezone.utc).isoformat()

        }
