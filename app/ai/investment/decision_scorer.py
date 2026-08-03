from datetime import datetime


class DecisionScorer:


    def score(

        self,

        research_score,

        roi_score,

        risk_score,

        strategic_fit=95

    ):


        investment_score = (

            research_score * 0.40

            +

            roi_score * 0.35

            +

            strategic_fit * 0.20

            -

            risk_score * 0.05

        )


        if investment_score >= 75:

            decision = "INVEST"

        elif investment_score >= 50:

            decision = "REVIEW"

        else:

            decision = "REJECT"



        return {


            "decision":

                decision,


            "investment_score":

                round(
                    investment_score,
                    2
                ),


            "strategic_fit":

                strategic_fit,


            "timestamp":

                datetime.utcnow().isoformat()

        }