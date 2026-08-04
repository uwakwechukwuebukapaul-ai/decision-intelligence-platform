from .intelligence_merger import IntelligenceMerger
from .investigation_builder import InvestigationBuilder
from .risk_combiner import RiskCombiner
from .fused_memory import FusedMemory
from .fused_logger import FusedLogger


class IntelligenceFusionEngine:
    """
    Sentinel DNA Intelligence Fusion Engine.

    Combines security intelligence
    into a unified investigation view.
    """


    def __init__(self):

        self.merger = IntelligenceMerger()

        self.builder = InvestigationBuilder()

        self.risk = RiskCombiner()

        self.memory = FusedMemory()

        self.logger = FusedLogger()



    def fuse(
        self,
        event,
        evidence=None,
        detection=None,
        threat=None,
        hunting=None,
        knowledge=None,
        cognitive=None
    ):


        merged = self.merger.merge(

            evidence,
            detection,
            threat,
            hunting,
            knowledge,
            cognitive

        )


        risk = self.risk.calculate(
            merged
        )


        investigation = self.builder.build(
            merged
        )


        memory = self.memory.store(
            investigation
        )


        log = self.logger.log(
            event
        )


        return {

            "status":
                "completed",

            "event":
                event,

            "risk":
                risk,

            "investigation":
                investigation,

            "memory":
                memory,

            "log":
                log

        }
