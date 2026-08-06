class KPICalculator:

    def calculate_score(self, metrics):

        score = 100

        score -= metrics["critical_threats"] * 10
        score -= metrics["active_incidents"] * 8
        score -= metrics["vulnerabilities"] * 5
        score -= metrics["identity_risks"] * 7
        score -= metrics["asset_exposure"] * 5

        score = max(score, 0)

        if score >= 80:
            level = "healthy"
        elif score >= 50:
            level = "moderate"
        else:
            level = "critical"

        return {
            "security_score": score,
            "security_level": level
        }