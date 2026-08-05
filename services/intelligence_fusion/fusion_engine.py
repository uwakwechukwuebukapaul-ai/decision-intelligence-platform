from .signal_processor import SignalProcessor
from .intelligence_correlator import IntelligenceCorrelator
from .context_builder import ContextBuilder
from .confidence_engine import ConfidenceEngine


class IntelligenceFusionEngine:
    """
    Sentinel DNA Intelligence Fusion Engine

    Combines multiple intelligence sources:

    - Evidence intelligence
    - Detection intelligence
    - Threat intelligence
    - Cognitive intelligence

    Produces unified intelligence context.
    """

    def __init__(self):

        self.signal_processor = SignalProcessor()

        self.correlator = IntelligenceCorrelator()

        self.context_builder = ContextBuilder()

        self.confidence_engine = ConfidenceEngine()


    def fuse(
        self,
        event,
        evidence=None,
        detection=None,
        threat=None,
        cognitive=None
    ):
        """
        Multi-source intelligence fusion pipeline.
        """

        evidence = evidence or {}

        detection = detection or {}

        threat = threat or {}

        cognitive = cognitive or {}


        signals = self.signal_processor.process(
            event,
            evidence=evidence,
            detection=detection,
            threat=threat,
            cognitive=cognitive
        )


        correlations = self.correlator.correlate(
            signals
        )


        context = self.context_builder.build(
            event,
            signals,
            correlations
        )


        confidence = self.confidence_engine.calculate(
            context
        )


        return {

            "status": "completed",

            "event": event,

            "signals": signals,

            "correlations": correlations,

            "context": context,

            "confidence": confidence,


            "risk": {

                "risk_level": (

                    cognitive.get(
                        "risk_level",
                        "unknown"
                    )

                ),

                "risk_score": (

                    evidence.get(
                        "risk_score",
                        0
                    )

                )

            },


            "fusion": {

                "engine": "IntelligenceFusionEngine",

                "sources": [

                    "evidence",

                    "detection",

                    "threat",

                    "cognitive"

                ]

            }

        }