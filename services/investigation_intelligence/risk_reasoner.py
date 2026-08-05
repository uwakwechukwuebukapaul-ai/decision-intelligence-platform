class RiskReasoner:
    """
    Autonomous security risk evaluation engine.
    """


    def assess(
        self,
        investigation
    ):

        score = 0
        factors = []


        text = str(
            investigation
        ).lower()


        if "ransomware" in text:

            score += 40

            factors.append(
                "Ransomware behavior detected"
            )


        if "powershell" in text:

            score += 20

            factors.append(
                "PowerShell execution detected"
            )


        if "database" in text:

            score += 20

            factors.append(
                "Critical database targeting detected"
            )


        if score >= 80:

            level = "CRITICAL"

        elif score >= 60:

            level = "HIGH"

        elif score >= 30:

            level = "MEDIUM"

        else:

            level = "LOW"



        return {

            "risk_level":
                level,

            "risk_score":
                score,

            "factors":
                factors

        }