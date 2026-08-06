class IdentityRiskAnalyzer:


    def analyze(self, identity):

        score = 20

        findings = []


        if identity["privilege_level"] in [
            "admin",
            "administrator"
        ]:

            score += 50

            findings.append(
                "Privileged identity detected"
            )


        if identity["role"] in [
            "administrator",
            "security_admin"
        ]:

            score += 20

            findings.append(
                "High impact role"
            )


        level = "low"


        if score >= 80:

            level = "critical"

        elif score >= 50:

            level = "high"


        return {

            "risk_score": score,

            "risk_level": level,

            "findings": findings

        }