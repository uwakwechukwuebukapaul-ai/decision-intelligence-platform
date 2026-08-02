from datetime import datetime

from .option_analyzer import OptionAnalyzer
from .impact_analyzer import ImpactAnalyzer
from .risk_reward_engine import RiskRewardEngine
from .decision_ranker import DecisionRanker
from .strategic_state import StrategicState



class StrategicController:


    def __init__(self, user_id):

        self.user_id = user_id

        self.option_analyzer = OptionAnalyzer()

        self.impact_analyzer = ImpactAnalyzer()

        self.risk_reward_engine = RiskRewardEngine()

        self.decision_ranker = DecisionRanker()

        self.strategic_state = StrategicState()



    def execute_strategic_cycle(self):


        options = self.option_analyzer.analyze(
            self.user_id
        )


        impacts = self.impact_analyzer.analyze(
            self.user_id,
            options["options"]
        )


        risk_reward = self.risk_reward_engine.evaluate(
            self.user_id,
            impacts
        )


        decision = self.decision_ranker.rank(
            self.user_id,
            impacts,
            risk_reward
        )


        state = self.strategic_state.generate(
            self.user_id
        )


        return {


            "user_id":
                self.user_id,


            "version":
                "1.0",


            "strategic_status":
                "active",


            "strategic_score":
                99,


            "generated_at":
                datetime.utcnow().isoformat(),


            "options_analysis":
                options,


            "impact_analysis":
                impacts,


            "risk_reward_analysis":
                risk_reward,


            "strategic_decision":
                decision,


            "system_state":
                state

        }