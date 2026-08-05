from .hypothesis_engine import HypothesisEngine
from .evidence_ranker import EvidenceRanker
from .investigation_plan import InvestigationPlan


class InvestigationReasoner:
    """
    Sentinel DNA autonomous investigation reasoning layer.
    """

    def __init__(self):

        self.hypothesis_engine = HypothesisEngine()

        self.evidence_ranker = EvidenceRanker()

        self.plan_builder = InvestigationPlan()



    def analyze(
        self,
        event
    ):

        hypotheses = self.hypothesis_engine.generate(
            event
        )


        evidence = []


        for hypothesis in hypotheses:

            evidence.extend(
                hypothesis["required_evidence"]
            )


        ranked_evidence = self.evidence_ranker.rank(
            evidence
        )


        plan = self.plan_builder.create(
            hypotheses
        )


        return {

            "status":
            "investigation_reasoned",

            "event":
            event,

            "hypotheses":
            hypotheses,

            "evidence_priority":
            ranked_evidence,

            "investigation_plan":
            plan

        }