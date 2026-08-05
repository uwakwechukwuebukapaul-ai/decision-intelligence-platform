class RiskReasoner:
    """
    AI risk reasoning layer.
    """


    def calculate(
        self,
        context
    ):

        score = 0


        if context.get("mitre_context"):
            score += 30


        if context.get("ioc_context"):
            score += 20


        if "ransomware" in context.get(
            "event",
            ""
        ).lower():

            score += 40


        if score >= 70:

            level = "CRITICAL"

        elif score >= 40:

            level = "HIGH"

        else:

            level = "LOW"



        return {

            "risk_score": score,

            "risk_level": level

        }