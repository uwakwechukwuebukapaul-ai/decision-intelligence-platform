"""
Sentinel DNA

IOC Reputation Engine

Responsible for:
- IOC reputation scoring
- Suspicion classification
- Intelligence source tracking

Designed for future integration with:
- VirusTotal
- AbuseIPDB
- MISP
- OpenCTI
- Internal threat feeds
"""


from __future__ import annotations



class ReputationEngine:
    """
    IOC reputation intelligence layer.
    """


    def analyze(
        self,
        indicator: dict,
    ) -> dict:
        """
        Analyze IOC reputation.
        """


        value = indicator.get(
            "indicator",
            "",
        )


        indicator_type = indicator.get(
            "type",
            "unknown",
        )


        reputation = "clean"

        confidence = 50

        sources = [
            "internal heuristic engine"
        ]


        suspicious_patterns = [

            ".xyz",
            ".top",
            ".click",
            ".zip",

        ]


        if any(
            value.endswith(pattern)
            for pattern in suspicious_patterns
        ):

            reputation = "suspicious"

            confidence = 85

            sources.append(
                "domain reputation heuristic"
            )


        elif indicator_type == "unknown":

            reputation = "unknown"

            confidence = 20



        return {

            "indicator":
                value,

            "reputation":
                reputation,

            "confidence":
                confidence,

            "sources":
                sources,

        }