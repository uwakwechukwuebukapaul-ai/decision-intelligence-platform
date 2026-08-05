from .event_bus import EventBus
from .context_manager import ContextManager
from .knowledge_graph import KnowledgeGraph
from .correlation_engine import CorrelationEngine
from .memory_fusion import MemoryFusion
from .intelligence_router import IntelligenceRouter


class SentinelIntelligenceFabric:

    def __init__(self):

        self.event_bus = EventBus()
        self.context_manager = ContextManager()
        self.knowledge_graph = KnowledgeGraph()
        self.correlation_engine = CorrelationEngine()
        self.memory_fusion = MemoryFusion()
        self.router = IntelligenceRouter()


    def process(self, event):

        self.event_bus.publish(event)

        context = self.context_manager.build(event)

        correlations = self.correlation_engine.correlate(
            context
        )

        self.knowledge_graph.add(
            context
        )

        self.memory_fusion.store(
            {
                "event": event,
                "context": context,
                "correlations": correlations
            }
        )

        return {
            "context": context,
            "correlations": correlations,
            "route": self.router.route(context)
        }