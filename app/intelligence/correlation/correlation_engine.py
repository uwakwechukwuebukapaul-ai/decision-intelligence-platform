"""
Sentinel DNA - Investigation Correlation Engine

Correlates intelligence from:

- IOC Fusion
- Investigation Memory
- Knowledge Graph
- Previous investigations
"""


from .correlation_result import (
    CorrelationResult,
)

from .correlation_rules import (
    CorrelationRules,
)

from .correlation_store import (
    CorrelationStore,
)





class CorrelationEngine:
    """
    Main correlation intelligence service.
    """



    def __init__(self):

        self.rules = CorrelationRules()

        self.store = CorrelationStore()





    def analyze(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Analyze intelligence relationships.
        """


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


        matches = []



        if self.rules.is_suspicious_domain(
            indicator
        ):

            matches.append(
                {
                    "type": "domain_pattern",
                    "indicator": indicator,
                    "reason": (
                        "Suspicious domain pattern detected"
                    ),
                }
            )



        previous = self.store.search(
            indicator
        )



        matches.extend(
            previous
        )



        confidence = 0


        if matches:

            confidence = min(
                50 + (len(matches) * 10),
                95,
            )



        result = CorrelationResult(

            indicator=indicator,

            correlated=bool(matches),

            confidence=confidence,

            matches=matches,

            recommendation=(
                "Escalate to threat hunting"
                if confidence >= 80
                else
                "Continue investigation"
            ),
        )


        return result.to_dict()