from .investigation_engine import InvestigationEngine
from .evidence_analyzer import EvidenceAnalyzer
from .hypothesis_manager import HypothesisManager
from .investigation_planner import InvestigationPlanner
from .graph_reasoner import GraphReasoner
from .case_intelligence import CaseIntelligence
from .runtime_orchestrator import RuntimeOrchestrator


class InvestigationGraphRuntime:
    """
    Sentinel DNA Investigation Graph Runtime.

    Coordinates autonomous investigation workflows by combining:
    - evidence analysis
    - hypothesis generation
    - investigation planning
    - graph reasoning
    - case intelligence
    """

    def __init__(self):
        self.engine = InvestigationEngine()
        self.evidence = EvidenceAnalyzer()
        self.hypothesis = HypothesisManager()
        self.planner = InvestigationPlanner()
        self.graph = GraphReasoner()
        self.case = CaseIntelligence()
        self.orchestrator = RuntimeOrchestrator()

    def investigate(self, alert):
        return self.orchestrator.execute(alert)