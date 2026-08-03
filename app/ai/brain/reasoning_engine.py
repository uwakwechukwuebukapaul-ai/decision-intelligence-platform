from datetime import datetime



class ReasoningEngine:


    def reason(

        self,

        context

    ):


        mission = context.get(
            "mission",
            ""
        )


        reasoning = []


        if "AI" in mission:

            reasoning.append(
                "Artificial intelligence opportunity detected"
            )


        if "security" in mission.lower():

            reasoning.append(
                "Security intelligence factor detected"
            )


        if not reasoning:

            reasoning.append(
                "General strategic reasoning applied"
            )


        return {

            "reasoning":

                reasoning,


            "confidence":

                min(
                    50 + len(reasoning) * 20,
                    95
                ),


            "timestamp":

                datetime.utcnow().isoformat()

        }