"""
Sentinel DNA - Correlation Rules
"""


class CorrelationRules:
    """
    Detection rules used by correlation engine.
    """



    SUSPICIOUS_TLDS = [

        ".xyz",
        ".top",
        ".click",
        ".zip",
        ".ru",

    ]



    def is_suspicious_domain(
        self,
        indicator: str,
    ) -> bool:


        indicator = indicator.lower()


        return any(

            indicator.endswith(tld)

            for tld in self.SUSPICIOUS_TLDS

        )