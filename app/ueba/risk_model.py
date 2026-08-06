class BehaviorRiskModel:


    def calculate(
        self,
        events
    ):

        score = 0
        reasons = []


        for event in events:

            if event["event_type"] == "failed_login":

                score += 30

                reasons.append(
                    "Multiple failed authentication attempts"
                )


            if event["event_type"] == "privileged_access":

                score += 50

                reasons.append(
                    "Privileged access behavior detected"
                )


        level = "low"


        if score >= 70:

            level = "critical"

        elif score >= 40:

            level = "high"


        return {

            "risk_score": score,

            "risk_level": level,

            "reasons": reasons

        }