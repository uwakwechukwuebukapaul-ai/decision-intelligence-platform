from app.ai.strategic_intelligence.recommendation_engine import RecommendationEngine
from app.ai.strategic_intelligence.strategy_memory import StrategyMemory



class StrategyEngine:
    """
    Main Strategic Intelligence Controller.
    """


    def __init__(self):

        self.recommendation = RecommendationEngine()

        self.memory = StrategyMemory()



    def analyze(
        self,
        mission,
        patterns=None,
        agents=None,
        knowledge=None
    ):


        result = self.recommendation.recommend(

            mission,

            patterns or [],

            agents or [],

            knowledge or []

        )


        stored = self.memory.save_strategy(

            mission,

            result["strategy"],

            result["confidence"],

            result["reasoning"]

        )


        return {


            "strategic_analysis":
                result,


            "memory":
                stored,


            "status":
                "completed"

        }