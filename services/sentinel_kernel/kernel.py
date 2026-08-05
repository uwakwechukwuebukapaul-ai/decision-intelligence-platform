from .engine_registry import EngineRegistry
from .intelligence_router import IntelligenceRouter
from .decision_orchestrator import DecisionOrchestrator
from .pipeline_controller import PipelineController


class SentinelKernel:
    """
    Sentinel DNA Central Intelligence Kernel.

    Entry point for autonomous security reasoning.
    """

    def __init__(self):

        self.registry = EngineRegistry()

        self.router = IntelligenceRouter(
            self.registry
        )

        self.decision_engine = DecisionOrchestrator()


        self.pipeline = PipelineController(
            self.router,
            self.decision_engine
        )


    def register_engine(
        self,
        name,
        engine
    ):
        self.registry.register(
            name,
            engine
        )


    def investigate(
        self,
        event
    ):

        return self.pipeline.execute(
            event
        )


    def status(self):

        return {
            "system":
                "Sentinel DNA Kernel",
            "engines":
                self.registry.status()
        }