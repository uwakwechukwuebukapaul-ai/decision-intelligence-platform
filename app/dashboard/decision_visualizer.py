from datetime import datetime



class DecisionVisualizer:



    def generate_summary(
        self,
        decision_result
    ):


        investment = (
            decision_result
            .get("decision_pipeline", {})
            .get("investment", {})
            .get("investment_analysis", {})
        )


        executive = (
            decision_result
            .get("decision_pipeline", {})
            .get("executive", {})
            .get("executive_advice", {})
        )



        return {


            "decision":

                investment.get(
                    "decision",
                    "UNKNOWN"
                ),


            "investment_score":

                investment.get(
                    "investment_score",
                    0
                ),


            "confidence":

                executive.get(
                    "confidence",
                    0
                ),


            "recommendation":

                executive.get(
                    "executive_recommendation",
                    "No recommendation"
                ),


            "timestamp":

                datetime.utcnow().isoformat()

        }