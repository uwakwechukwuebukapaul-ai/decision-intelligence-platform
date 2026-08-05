import datetime

from .investigation_context import InvestigationContext
from .investigation_manager import InvestigationManager
from .engine_orchestrator import EngineOrchestrator
from .result_aggregator import ResultAggregator
from .runtime_memory import RuntimeMemory
from .runtime_logger import RuntimeLogger


class InvestigationRuntimeEngine:
    """
    Sentinel DNA Unified Investigation Runtime.

    Main autonomous investigation execution boundary.

    Responsibilities:
    - Create investigation context
    - Start investigation lifecycle
    - Execute intelligence engines
    - Aggregate results
    - Store runtime memory
    - Produce investigation logs

    Compatibility:
    - Keeps legacy "engines" response key
    - Adds new "intelligence" response layer
    """


    def __init__(self):

        self.context_engine = InvestigationContext()

        self.manager = InvestigationManager()

        self.orchestrator = EngineOrchestrator()

        self.aggregator = ResultAggregator()

        self.memory = RuntimeMemory()

        self.logger = RuntimeLogger()



    def investigate(
        self,
        event
    ):

        # Create investigation context

        context = self.context_engine.create(
            event
        )


        # Start investigation lifecycle

        investigation = self.manager.start(
            context
        )


        # Execute intelligence layers
        #
        # Includes:
        # - Investigation Graph Runtime
        # - Cognitive Investigation Engine
        # - Evidence Intelligence
        # - Threat Hunting
        # - Knowledge Graph
        # - SOAR

        intelligence = self.orchestrator.execute(
            event
        )


        # Aggregate final investigation result

        result = self.aggregator.aggregate(
            context,
            investigation,
            intelligence
        )


        # Store memory

        memory = self.memory.store(
            result
        )


        # Create audit log

        log = self.logger.log(
            event
        )


        return {


            "status":
                "completed",


            "event":
                event,


            "context":
                context,


            "investigation":
                investigation,


            #
            # New enterprise intelligence output
            #
            "intelligence":
                intelligence,


            #
            # Backward compatibility
            #
            # Existing Sentinel DNA services
            # consume this key.
            #
            "engines":
                intelligence,


            "result":
                result,


            "memory":
                memory,


            "log":
                log,


            "created_at":
                datetime.datetime.now(
                    datetime.timezone.utc
                ).isoformat()

        }



    def execute(
        self,
        event
    ):
        """
        Compatibility interface.

        Sentinel Core expects runtime
        engines to expose execute().
        """

        return self.investigate(
            event
        )