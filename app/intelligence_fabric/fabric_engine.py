from datetime import datetime

from .engine_registry import EngineRegistry
from .intelligence_router import IntelligenceRouter
from .event_bus import EventBus
from .data_pipeline import DataPipeline
from .context_manager import ContextManager
from .decision_fusion import DecisionFusion
from .fabric_memory import FabricMemory
from .fabric_logger import FabricLogger



class IntelligenceFabricEngine:


    def __init__(self):

        self.registry = EngineRegistry()

        self.router = IntelligenceRouter()

        self.event_bus = EventBus()

        self.pipeline = DataPipeline()

        self.context = ContextManager()

        self.decision = DecisionFusion()

        self.memory = FabricMemory()

        self.logger = FabricLogger()



    def process(self, event):


        published_event = self.event_bus.publish(
            event
        )


        pipeline_result = self.pipeline.process(
            event
        )


        context = self.context.create(
            event
        )


        routing = self.router.route(
            event
        )


        engines = self.registry.list_engines()


        decision = self.decision.analyze(
            event
        )


        memory = self.memory.store(
            event
        )


        log = self.logger.log(
            event
        )


        return {


            "status":
            "completed",


            "event":
            event,


            "event_bus":
            published_event,


            "pipeline":
            pipeline_result,


            "context":
            context,


            "routing":
            routing,


            "engines":
            engines,


            "decision":
            decision,


            "memory":
            memory,


            "log":
            log,


            "created_at":
            datetime.utcnow().isoformat()

        }