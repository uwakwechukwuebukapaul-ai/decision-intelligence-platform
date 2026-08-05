from .evidence_collector import EvidenceCollector
from .confidence_calculator import ConfidenceCalculator



class EvidenceFusionEngine:
    """
    Combines multiple security signals
    into a unified investigation verdict.
    """


    def __init__(self):

        self.collector = EvidenceCollector()

        self.confidence = ConfidenceCalculator()



    def add_evidence(
        self,
        evidence_type,
        data,
        source,
        weight
    ):


        item = self.collector.collect(

            evidence_type,

            data,

            source

        )


        item.assign_weight(
            weight
        )


        return item



    def analyze(
        self
    ):


        evidence = self.collector.all()


        confidence = self.confidence.calculate(

            evidence

        )


        verdict = "low"



        if confidence >= 80:

            verdict = "critical"


        elif confidence >= 50:

            verdict = "high"


        elif confidence >= 25:

            verdict = "medium"



        return {

            "evidence_count":
            len(evidence),

            "confidence":
            confidence,

            "verdict":
            verdict,

            "evidence":
            evidence

        }