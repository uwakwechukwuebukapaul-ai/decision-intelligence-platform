from datetime import datetime



class StrategyRecommender:



    def recommend(
        self,
        question,
        investment_score,
        market_signal
    ):


        if investment_score >= 75:


            recommendation = (
                "Execute AI SOC automation market entry strategy"
            )


            strategy = [

                "Build AI-native SOC investigation platform",

                "Focus on autonomous alert investigation",

                "Reduce analyst alert fatigue",

                "Target enterprise security operations teams",

                "Differentiate through AI reasoning capability"

            ]


        elif investment_score >= 50:


            recommendation = (
                "Continue validation before major investment"
            )


            strategy = [

                "Validate customer demand",

                "Expand market research",

                "Build smaller proof-of-value product"

            ]


        else:


            recommendation = (
                "Delay investment decision"
            )


            strategy = [

                "Reduce business risk",

                "Collect additional evidence",

                "Reevaluate opportunity"

            ]



        return {


            "question":
                question,


            "recommendation":
                recommendation,


            "strategy":
                strategy,


            "market_signal":
                market_signal,


            "timestamp":
                datetime.utcnow().isoformat()

        }