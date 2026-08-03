from datetime import datetime


class ReasoningEngine:

    def __init__(self):
        pass


    def reason(self, context):

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


        confidence = min(
            50 + len(reasoning) * 20,
            95
        )


        return {

            "reasoning": reasoning,

            "confidence": confidence,

            "timestamp":
                datetime.utcnow().isoformat()

        }


    # compatibility method
    # supports older v63 brain calls

    def analyze(self, context):

        return self.reason(context)