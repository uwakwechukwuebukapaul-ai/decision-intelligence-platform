"""
Sentinel DNA Risk Propagation Engine.
"""


class RiskPropagationEngine:
    """
    Calculates compromise impact propagation.
    """



    def calculate(
        self,
        entities
    ):

        entity_count = len(
            entities
        )


        risk_score = entity_count * 25


        if risk_score > 100:

            risk_score = 100



        return {

            "risk_score":
                risk_score,


            "impact":

                "critical"

                if risk_score >= 75

                else

                "high"

                if risk_score >= 50

                else

                "medium",


            "entities_analyzed":
                entity_count

        }