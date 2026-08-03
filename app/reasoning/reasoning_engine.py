from datetime import datetime

from .chain_of_thought import ReasoningChain
from .risk_reasoner import RiskReasoner
from .decision_reasoner import DecisionReasoner
from .strategy_reasoner import StrategyReasoner
from .confidence_reasoner import ConfidenceReasoner
from .reasoning_memory import ReasoningMemory



class ReasoningEngine:
    """
    Sentinel DNA Autonomous Reasoning Engine.

    Connects:
    Knowledge
    Risk
    Decision
    Strategy
    Confidence
    Memory
    """

    def __init__(self):

        self.chain = ReasoningChain()
        self.risk = RiskReasoner()
        self.decision = DecisionReasoner()
        self.strategy = StrategyReasoner()
        self.confidence = ConfidenceReasoner()
        self.memory = ReasoningMemory()



    def reason(self, question):


        reasoning = self.chain.build(
            question
        )


        risk = self.risk.analyze(
            question
        )


        decision = self.decision.decide(
            risk
        )


        strategy = self.strategy.recommend(
            decision
        )


        confidence = self.confidence.calculate(
            risk,
            reasoning
        )


        result = {

            "status":
                "completed",

            "question":
                question,


            "risk":
                risk,


            "decision":
                decision,


            "strategy":
                strategy,


            "reasoning":
                reasoning,


            "confidence":
                confidence,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return result