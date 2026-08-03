from datetime import datetime


from app.ai.investment.risk_analyzer import RiskAnalyzer
from app.ai.investment.roi_analyzer import ROIAnalyzer
from app.ai.investment.decision_scorer import DecisionScorer
from app.ai.investment.investment_memory import InvestmentMemory



class InvestmentEngine:


    def __init__(self):

        self.risk = RiskAnalyzer()

        self.roi = ROIAnalyzer()

        self.scorer = DecisionScorer()

        self.memory = InvestmentMemory()



    def evaluate(
        self,
        question,
        research,
        predictions=None,
        simulations=None
    ):


        market_score = research.get(
            "market_score",
            0
        )


        risk_analysis = self.risk.analyze(
            research
        )


        roi_analysis = self.roi.analyze(
            research
        )


        decision = self.scorer.score(

            market_score,

            roi_analysis["roi_score"],

            risk_analysis["risk_score"]

        )


        result = {

            "question":
                question,


            "decision":
                decision["decision"],


            "investment_score":
                decision["investment_score"],


            "reasoning":

                [
                    "Market opportunity evaluated",

                    "ROI potential analyzed",

                    "Business risks assessed"
                ],


            "risk_analysis":
                risk_analysis,


            "roi_analysis":
                roi_analysis,


            "confidence":
                90,


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return {

            "status":
                "completed",

            "investment_analysis":
                result

        }