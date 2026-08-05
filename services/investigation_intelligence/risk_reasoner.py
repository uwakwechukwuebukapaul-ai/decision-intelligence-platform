class RiskReasoner:
    """
    Sentinel DNA Autonomous Security Risk Reasoner.

    Uses:

    - Current investigation evidence
    - Historical memory context
    - Threat patterns
    - Security knowledge

    to calculate risk.
    """


    def assess(
        self,
        investigation,
        memory_context=None
    ):

        score = 0

        factors = []


        text = str(
            investigation
        ).lower()



        #
        # Current investigation signals
        #

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



        #
        # Memory intelligence signals
        #

        if memory_context:


            incidents = memory_context.get(
                "similar_incidents",
                []
            )


            patterns = memory_context.get(
                "known_patterns",
                []
            )


            knowledge = memory_context.get(
                "previous_memories",
                []
            )



            if incidents:

                score += 15

                factors.append(
                    "Historical incident match detected"
                )



            if patterns:

                score += 15

                factors.append(
                    "Known attack pattern detected"
                )



            if knowledge:

                score += 10

                factors.append(
                    "Security knowledge correlation found"
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