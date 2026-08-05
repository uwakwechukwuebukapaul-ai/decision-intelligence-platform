from .investigation_model import InvestigationModel
from .evidence_analyzer import EvidenceAnalyzer
from .timeline_builder import TimelineBuilder
from .recommendation_engine import RecommendationEngine



class InvestigationAIEngine:
    """
    Sentinel DNA Autonomous Investigation AI Engine.

    Combines:
    - case creation
    - evidence intelligence
    - timeline analysis
    - recommendations
    """


    def __init__(self):

        self.model = InvestigationModel()

        self.evidence = EvidenceAnalyzer()

        self.timeline = TimelineBuilder()

        self.recommendations = RecommendationEngine()



    def investigate(self, event):

        case = self.model.create_case(event)


        evidence = self.evidence.analyze(event)


        timeline = self.timeline.build(
            [
                event
            ]
        )


        recommendations = self.recommendations.recommend(
            event
        )


        return {

            "case": case,

            "evidence": evidence,

            "timeline": timeline,

            "recommendations": recommendations,

            "status":
                "investigation_completed"

        }



    # compatibility API
    def analyze(self, event):

        return self.investigate(event)