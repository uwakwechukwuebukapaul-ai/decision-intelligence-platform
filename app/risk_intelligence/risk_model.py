class RiskModel:


    def determine_level(self, score):

        if score >= 90:
            return "critical"

        if score >= 70:
            return "high"

        if score >= 40:
            return "medium"

        return "low"