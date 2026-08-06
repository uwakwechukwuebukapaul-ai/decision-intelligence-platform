class RiskFusion:


    def calculate(self, signals):

        score = 0
        findings = []


        if signals.get("severity") == "critical":

            score += 40

            findings.append(
                "Critical threat severity"
            )


        if signals.get("indicator"):

            score += 25

            findings.append(
                "Malicious indicator detected"
            )


        if signals.get("asset"):

            score += 20

            findings.append(
                "Asset exposure identified"
            )


        if signals.get("identity"):

            score += 15

            findings.append(
                "Identity risk detected"
            )


        if score >= 80:

            level = "critical"

        elif score >= 60:

            level = "high"

        elif score >= 40:

            level = "medium"

        else:

            level = "low"


        return {
            "risk_score": score,
            "risk_level": level,
            "findings": findings
        }