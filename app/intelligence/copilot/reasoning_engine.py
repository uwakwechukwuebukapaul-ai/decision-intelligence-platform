"""
Sentinel DNA

AI SOC Copilot Reasoning Engine

Combines intelligence,
explanations, and recommendations.
"""


from .explanation_engine import (
    ExplanationEngine,
)


from .recommendation_engine import (
    RecommendationEngine,
)



class CopilotReasoningEngine:


    def __init__(self):

        self.explainer = ExplanationEngine()

        self.recommender = RecommendationEngine()



    def analyze(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate analyst copilot response.
        """


        return {

            "copilot":

                "Sentinel DNA AI Investigation Assistant",


            "explanation":

                self.explainer.explain(
                    intelligence
                ),


            "recommendations":

                self.recommender.generate(
                    intelligence
                ),

        }