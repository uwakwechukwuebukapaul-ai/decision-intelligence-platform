import datetime
import uuid

from services.investigation_graph_runtime import InvestigationGraphRuntime
from services.cognitive_investigation_engine import (
    CognitiveInvestigationEngine,
)


class EngineOrchestrator:
    """
    Sentinel DNA Investigation Engine Orchestrator.

    Converts raw events into investigation objects
    and coordinates intelligence layers.
    """

    def __init__(self):

        self.graph_runtime = InvestigationGraphRuntime()

        self.cognitive_engine = CognitiveInvestigationEngine()



    def normalize_event(self, event):

        if isinstance(event, dict):

            return event


        return {

            "id":
                f"INV-{uuid.uuid4().hex[:8].upper()}",

            "severity":
                "unknown",

            "description":
                event,

            "source":
                "autonomous_runtime"

        }



    def execute(self, event):


        investigation_event = self.normalize_event(
            event
        )


        graph_result = self.graph_runtime.investigate(
            investigation_event
        )


        if hasattr(
            self.cognitive_engine,
            "analyze"
        ):

            cognitive_result = self.cognitive_engine.analyze(
                investigation_event
            )

        else:

            cognitive_result = {

                "status":
                    "available",

                "engine":
                    "Cognitive Investigation Engine"

            }



        return {


            "engines_executed": [

                "Investigation Graph Runtime",

                "Cognitive Investigation Engine",

                "Evidence Intelligence",

                "Threat Hunting",

                "Knowledge Graph",

                "Intelligence Fusion",

                "SOAR"

            ],


            "event":
                investigation_event,


            "graph_investigation":
                graph_result,


            "cognitive_analysis":
                cognitive_result,


            "status":
                "completed",


            "timestamp":
                datetime.datetime.now(
                    datetime.timezone.utc
                ).isoformat()

        }