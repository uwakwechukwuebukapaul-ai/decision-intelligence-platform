class ActionRecommender:

    def recommend(self, risk_level):

        actions = {
            "critical": [
                "contain threat",
                "isolate affected assets",
                "start incident response"
            ],
            "high": [
                "investigate indicators",
                "collect evidence"
            ],
            "medium": [
                "monitor activity",
                "review telemetry"
            ],
            "low": [
                "continue monitoring"
            ]
        }

        return actions.get(
            risk_level,
            ["monitor"]
        )