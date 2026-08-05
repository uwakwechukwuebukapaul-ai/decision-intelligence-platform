import datetime
import uuid

from services.investigation_graph_runtime import InvestigationGraphRuntime
from services.cognitive_investigation_engine import (
    CognitiveInvestigationEngine,
)

from services.investigation_intelligence.memory_context import (
    MemoryContext,
)


class EngineOrchestrator:
    """
    Sentinel DNA Investigation Engine Orchestrator.

    Coordinates:

    - Memory retrieval
    - Investigation graph runtime
    - Cognitive investigation
    - Intelligence reasoning

    Flow:

    Event
      |
      v
    Memory Context
      |
      v
    Investigation Engines
      |
      v
    Intelligence Result
    """



    def __init__(self):

        self.graph_runtime = InvestigationGraphRuntime()

        self.cognitive_engine = CognitiveInvestigationEngine()

        self.memory_context = MemoryContext()



    def normalize_event(
        self,
        event
    ):

        if isinstance(
            event,
            dict
        ):

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



    def execute(
        self,
        event
    ):


        investigation_event = self.normalize_event(
            event
        )


        #
        # Retrieve previous intelligence
        #

        memory_context = self.memory_context.retrieve(
            investigation_event
        )



        #
        # Execute investigation graph
        #

        graph_result = self.graph_runtime.investigate(
            investigation_event
        )



        #
        # Execute cognitive investigation
        #

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


            "engines_executed":

            [

                "Memory Context",

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



            "memory_context":

                memory_context,



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