class PostureCalculator:

    def calculate(self, signals):
        score = 100
        findings = []

        if signals.get("critical_threats", 0) > 0:
            score -= 25
            findings.append("Critical threats detected")

        if signals.get("vulnerabilities", 0) > 0:
            score -= 20
            findings.append("Unresolved vulnerabilities detected")

        if signals.get("identity_risk", False):
            score -= 20
            findings.append("Identity security risks detected")

        if signals.get("asset_exposure", False):
            score -= 15
            findings.append("Critical asset exposure detected")

        if signals.get("detection_gap", False):
            score -= 10
            findings.append("Detection coverage gaps detected")

        score = max(score, 0)

        if score >= 80:
            level = "healthy"
        elif score >= 60:
            level = "moderate"
        elif score >= 40:
            level = "high"
        else:
            level = "critical"

        return {
            "score": score,
            "level": level,
            "findings": findings
        }