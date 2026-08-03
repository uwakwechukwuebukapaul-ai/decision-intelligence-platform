from datetime import datetime


class DecisionScorer:


    def score(

        self,

        research_score,

        roi_score,

        risk_score

    ):


        investment_score = (

            research_score * 0.4

            +

            roi_score * 0.4

            -

            risk_score * 0.2

        )


        if investment_score >= 70:

            decision = "INVEST"

        else:

            decision = "REVIEW"


        return {


            "decision":
                decision,


            "investment_score":
                round(
                    investment_score,
                    2
                ),


            "timestamp":
                datetime.utcnow().isoformat()

        }