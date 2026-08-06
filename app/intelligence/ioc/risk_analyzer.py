"""
Sentinel DNA

IOC Risk Analyzer

Responsible for:
- IOC risk scoring
- Suspicion classification
- Security context generation
"""


class RiskAnalyzer:
    """
    Calculates IOC risk.
    """


    def analyze(
        self,
        indicator: dict,
    ) -> dict:
        """
        Analyze parsed indicator.
        """


        indicator_type = indicator.get(
            "type"
        )

        value = indicator.get(
            "value",
            "",
        )


        score = 0

        reasons = []


        # IP analysis

        if indicator_type == "ip":

            score += 10

            reasons.append(
                "IP indicator analyzed"
            )


        # Domain analysis

        elif indicator_type == "domain":

            score += 20

            reasons.append(
                "Domain indicator analyzed"
            )


            suspicious_tlds = [

                ".xyz",
                ".top",
                ".click",
                ".zip",
                ".ru",

            ]


            if any(
                value.endswith(tld)
                for tld in suspicious_tlds
            ):

                score += 40

                reasons.append(
                    "Suspicious domain extension"
                )


        else:

            score += 5

            reasons.append(
                "Unknown indicator type"
            )



        if score >= 60:

            risk = "high"

        elif score >= 30:

            risk = "medium"

        else:

            risk = "low"



        return {

            "score": score,

            "risk": risk,

            "reasons": reasons,

        }