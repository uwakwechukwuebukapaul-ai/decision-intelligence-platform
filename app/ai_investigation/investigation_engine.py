from datetime import datetime

from .case_analyzer import CaseAnalyzer
from .evidence_reasoner import EvidenceReasoner
from .threat_reasoner import ThreatReasoner
from .investigation_planner import InvestigationPlanner
from .root_cause_analyzer import RootCauseAnalyzer
from .recommendation_engine import RecommendationEngine
from .investigation_memory import InvestigationMemory
from .investigation_logger import InvestigationLogger


class AIInvestigationEngine:

    def __init__(self):

        self.case = CaseAnalyzer()
        self.evidence = EvidenceReasoner()
        self.threat = ThreatReasoner()
        self.planner = InvestigationPlanner()
        self.root = RootCauseAnalyzer()
        self.recommendations = RecommendationEngine()
        self.memory = InvestigationMemory()
        self.logger = InvestigationLogger()


    def investigate(self, incident):

        case_analysis = self.case.analyze(
            incident
        )

        evidence = self.evidence.analyze(
            incident
        )

        threat = self.threat.analyze(
            incident
        )

        plan = self.planner.create_plan(
            incident
        )

        root = self.root.analyze(
            incident
        )

        recommendations = self.recommendations.generate(
            incident
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.log(
            incident
        )


        return {

            "status":
                "completed",

            "incident":
                incident,

            "case_analysis":
                case_analysis,

            "evidence_analysis":
                evidence,

            "threat_analysis":
                threat,

            "investigation_plan":
                plan,

            "root_cause":
                root,

            "recommendations":
                recommendations,

            "memory":
                memory,

            "log":
                log,

            "created_at":
                datetime.utcnow().isoformat()
        }