from datetime import datetime

from .data_normalizer import DataNormalizer
from .signal_correlator import SignalCorrelator
from .context_builder import ContextBuilder
from .risk_aggregator import RiskAggregator
from .decision_fusion import DecisionFusion
from .fusion_memory import FusionMemory



class FusionEngine:
    """
    Sentinel DNA Intelligence Fusion Engine.

    Combines all security intelligence sources
    into one unified decision layer.
    """


    def __init__(self):

        self.normalizer = DataNormalizer()

        self.correlator = SignalCorrelator()

        self.context_builder = ContextBuilder()

        self.risk_engine = RiskAggregator()

        self.decision_engine = DecisionFusion()

        self.memory = FusionMemory()



    def analyze(self, security_input):


        normalized = self.normalizer.normalize(
            {
                "event": security_input,
                "source": "Sentinel DNA"
            }
        )


        correlation = self.correlator.correlate(
            security_input
        )


        context = self.context_builder.build(
            security_input
        )


        risk = self.risk_engine.calculate(
            security_input
        )


        decision = self.decision_engine.decide(
            risk
        )


        result = {

            "status": "completed",

            "input": security_input,

            "normalization": normalized,

            "signal_correlation": correlation,

            "context": context,

            "risk": risk,

            "decision": decision,

            "created_at": datetime.utcnow().isoformat()

        }


        self.memory.store(result)


        return result