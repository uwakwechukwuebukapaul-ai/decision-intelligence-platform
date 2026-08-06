class IdentityRiskAnalyzer:


    def analyze(self, identity):

        score = 0
        reasons = []


        if identity["privilege_level"] == "admin":

            score += 50
            reasons.append(
                "Privileged identity detected"
            )


        if identity["role"] in [
            "administrator",
            "security_admin"
        ]:

            score += 30
            reasons.append(
                "High impact role"
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