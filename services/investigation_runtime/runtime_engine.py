import datetime

from .investigation_context import InvestigationContext
from .investigation_manager import InvestigationManager
from .engine_orchestrator import EngineOrchestrator
from .result_aggregator import ResultAggregator
from .runtime_memory import RuntimeMemory
from .runtime_logger import RuntimeLogger


class InvestigationRuntimeEngine:

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

        context = self.context_engine.create(
            event
        )


        investigation = self.manager.start(
            context
        )


        engines = self.orchestrator.execute(
            event
        )


        result = self.aggregator.aggregate(
            context,
            investigation,
            engines
        )


        memory = self.memory.store(
            result
        )


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

            "engines":
                engines,

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
        Compatibility interface for Sentinel Core.

        Sentinel Core expects every runtime engine
        to expose execute().
        """

        return self.investigate(
            event
        )