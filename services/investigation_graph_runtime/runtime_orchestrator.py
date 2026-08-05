from .investigation_engine import InvestigationEngine
from .evidence_analyzer import EvidenceAnalyzer
from .hypothesis_manager import HypothesisManager
from .investigation_planner import InvestigationPlanner
from .graph_reasoner import GraphReasoner
from .case_intelligence import CaseIntelligence


class RuntimeOrchestrator:
    """
    Coordinates autonomous investigation workflow.
    """

    def __init__(self):

        self.engine = InvestigationEngine()
        self.evidence = EvidenceAnalyzer()
        self.hypothesis = HypothesisManager()
        self.planner = InvestigationPlanner()
        self.graph = GraphReasoner()
        self.case = CaseIntelligence()


    def execute(self, alert):

        investigation = self.engine.start(
            alert
        )

        evidence = self.evidence.analyze(
            alert
        )

        hypothesis = self.hypothesis.create(
            evidence
        )

        plan = self.planner.build(
            hypothesis
        )

        graph = self.graph.analyze(
            alert.get(
                "entities",
                []
            )
        )

        result = self.case.build(
            investigation,
            evidence,
            hypothesis,
            plan,
            graph
        )

        return self.engine.complete(
            result
        )