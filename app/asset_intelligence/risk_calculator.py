class AssetRiskCalculator:


    def calculate(self, asset):

        score = 20
        reasons = []


        if asset["criticality"] == "critical":
            score += 60
            reasons.append(
                "Critical business asset"
            )


        elif asset["criticality"] == "high":
            score += 40
            reasons.append(
                "High value asset"
            )


        level = "low"


        if score >= 80:
            level = "critical"

        elif score >= 50:
            level = "high"


        return {

            "risk_score": score,

            "risk_level": level,

            "reasons": reasons

        }