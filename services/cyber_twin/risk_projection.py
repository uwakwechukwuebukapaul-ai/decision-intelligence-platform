class RiskProjection:
    """
    Predicts future security risk.
    """


    def calculate(
        self,
        threats=None,
        vulnerabilities=None,
        controls=None
    ):

        threat_score = len(threats or [])

        vulnerability_score = len(vulnerabilities or [])

        control_score = len(controls or [])


        risk = (
            threat_score * 40
            +
            vulnerability_score * 30
            -
            control_score * 10
        )


        return {

            "risk_score": max(risk, 0),

            "risk_level":

                "critical"
                if risk >= 80
                else
                "high"
                if risk >= 50
                else
                "medium"

        }