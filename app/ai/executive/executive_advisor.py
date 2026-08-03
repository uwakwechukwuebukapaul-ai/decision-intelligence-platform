from datetime import datetime

from app.ai.executive.strategy_recommender import (
    StrategyRecommender
)

from app.ai.executive.market_entry_planner import (
    MarketEntryPlanner
)

from app.ai.executive.executive_memory import (
    ExecutiveMemory
)


class ExecutiveAdvisor:


    def __init__(self):

        self.strategy_engine = StrategyRecommender()

        self.market_engine = MarketEntryPlanner()

        self.memory = ExecutiveMemory()



    def advise(
        self,
        question,
        investment_analysis
    ):


        investment_score = investment_analysis.get(
            "investment_score",
            0
        )


        strategy = self.strategy_engine.recommend(
            question,
            investment_score,
            "Strong AI SOC automation opportunity"
        )


        market_plan = self.market_engine.create_plan(
            "AI SOC Cybersecurity Market"
        )


        executive_report = {


            "question":
                question,


            "executive_recommendation":
                strategy["recommendation"],


            "strategic_priorities":
                strategy["strategy"],


            "market_entry_plan":
                market_plan,


            "investment_signal":
                investment_score,


            "confidence":
                92,


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            executive_report
        )


        return {


            "status":
                "completed",


            "executive_advice":
                executive_report

        }