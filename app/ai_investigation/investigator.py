"""
Sentinel DNA AI Investigator

Main investigation orchestrator.
"""


from .finding_engine import FindingEngine
from .reasoning_engine import ReasoningEngine
from .recommendation_engine import RecommendationEngine



class AIInvestigator:


    def __init__(self):

        self.findings = FindingEngine()

        self.reasoning = ReasoningEngine()

        self.recommendations = (
            RecommendationEngine()
        )



    def investigate(
        self,
        context: dict,
    ):


        return {

            "incident":
                context.get(
                    "incident"
                ),


            "findings":
                self.findings.generate(
                    context
                ),


            "reasoning":
                self.reasoning.analyze(
                    context
                ),


            "recommendations":
                self.recommendations.generate(
                    context
                ),

        }