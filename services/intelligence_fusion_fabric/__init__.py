from .fusion_engine import FusionEngine
from .signal_correlator import SignalCorrelator
from .context_builder import ContextBuilder
from .entity_resolver import EntityResolver
from .confidence_fusion import ConfidenceFusion
from .intelligence_router import IntelligenceRouter
from .fusion_orchestrator import FusionOrchestrator


class IntelligenceFusionFabric:

    def __init__(self):

        self.fusion_engine = FusionEngine()
        self.signal_correlator = SignalCorrelator()
        self.context_builder = ContextBuilder()
        self.entity_resolver = EntityResolver()
        self.confidence_fusion = ConfidenceFusion()
        self.intelligence_router = IntelligenceRouter()
        self.orchestrator = FusionOrchestrator()


    def fuse(self, intelligence):

        return self.orchestrator.process(intelligence)