class RiskCombiner:
    """
    Calculates unified security risk.
    """

    def calculate(self, intelligence):

        risk_score = 0


        text = str(
            intelligence
        ).lower()


        if "ransomware" in text:
            risk_score += 40


        if "powershell" in text:
            risk_score += 20


        if "critical" in text:
            risk_score += 40



        if risk_score >= 80:

            level = "critical"

        elif risk_score >= 50:

            level = "high"

        else:

            level = "medium"



        return {

            "risk_score":
                risk_score,

            "risk_level":
                level

        }