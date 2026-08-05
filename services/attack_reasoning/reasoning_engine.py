"""
Sentinel DNA Autonomous Attack Reasoning Engine.
"""


from .attack_path import AttackPathAnalyzer

from .risk_propagation import RiskPropagationEngine

from .decision_model import SecurityDecisionModel



class AttackReasoningEngine:
    """
    High level attack reasoning controller.
    """



    def __init__(self):

        self.attack_path = AttackPathAnalyzer()

        self.risk_engine = RiskPropagationEngine()

        self.decision_model = SecurityDecisionModel()



    def analyze(
        self,
        entities
    ):


        attack_path = self.attack_path.analyze(
            entities
        )


        risk = self.risk_engine.calculate(
            entities
        )


        decision = self.decision_model.decide(
            risk["risk_score"]
        )


        return {

            "attack_path":
                attack_path,


            "risk":
                risk,


            "decision":
                decision,


            "status":
                "attack_reasoning_completed"

        }



    def process(
        self,
        entities
    ):

        """
        Sentinel Core compatibility interface.
        """

        return self.analyze(
            entities
        )