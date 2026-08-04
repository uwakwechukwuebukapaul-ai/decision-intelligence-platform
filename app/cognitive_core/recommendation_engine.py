from datetime import datetime


class RecommendationEngine:

    def recommend(self, decision):

        priority = decision.get(
            "priority"
        )


        if priority == "critical":

            actions = [
                "Isolate affected systems",
                "Block malicious indicators",
                "Collect forensic evidence",
                "Begin incident response workflow"
            ]


        elif priority == "high":

            actions = [
                "Investigate affected assets",
                "Review security logs",
                "Validate indicators"
            ]


        else:

            actions = [
                "Monitor activity",
                "Continue analysis"
            ]


        return {

            "recommended_actions": actions,

            "generated_from":
                decision.get(
                    "decision"
                ),

            "timestamp":
                datetime.utcnow().isoformat()
        }