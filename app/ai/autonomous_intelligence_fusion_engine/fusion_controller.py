from datetime import datetime

from .intelligence_collector import IntelligenceCollector
from .decision_synthesizer import DecisionSynthesizer
from .confidence_engine import ConfidenceEngine
from .recommendation_engine import RecommendationEngine
from .fusion_state import FusionState



class FusionController:


    def __init__(self, user_id):

        self.user_id = user_id

        self.collector = IntelligenceCollector()

        self.synthesizer = DecisionSynthesizer()

        self.confidence = ConfidenceEngine()

        self.recommendation = RecommendationEngine()

        self.state = FusionState()



    def execute_fusion_cycle(self):


        intelligence = self.collector.collect(
            self.user_id
        )


        decision = self.synthesizer.synthesize(
            intelligence
        )


        confidence = self.confidence.calculate(
            decision
        )


        recommendation = self.recommendation.recommend(
            decision,
            confidence
        )


        state = self.state.generate(
            self.user_id
        )


        return {


            "user_id":
                self.user_id,


            "fusion_status":
                "active",


            "fusion_score":
                99,


            "intelligence_collection":
                intelligence,


            "decision_analysis":
                decision,


            "confidence_analysis":
                confidence,


            "recommendation":
                recommendation,


            "system_state":
                state,


            "generated_at":
                datetime.utcnow().isoformat(),


            "version":
                "1.0"

        }