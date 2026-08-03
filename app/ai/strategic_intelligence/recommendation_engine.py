from datetime import datetime


class RecommendationEngine:
    """
    Generates strategic recommendations.
    """



    def recommend(
        self,
        mission,
        patterns,
        agents,
        knowledge
    ):


        reasoning = []


        confidence = 50



        if patterns:

            reasoning.append(
                "Historical successful patterns detected"
            )

            confidence += 15



        if agents:

            reasoning.append(
                "High performing agents available"
            )

            confidence += 15



        if knowledge:

            reasoning.append(
                "Relevant knowledge discovered"
            )

            confidence += 10



        if confidence >= 80:

            strategy = (
                "Execute recommended strategy using "
                "high-performing intelligence resources"
            )


        elif confidence >= 60:

            strategy = (
                "Proceed with controlled execution "
                "and additional validation"
            )


        else:

            strategy = (
                "Collect more intelligence before execution"
            )



        return {


            "mission":
                mission,


            "strategy":
                strategy,


            "confidence":
                min(
                    confidence,
                    95
                ),


            "reasoning":
                reasoning,


            "timestamp":
                datetime.utcnow().isoformat()

        }