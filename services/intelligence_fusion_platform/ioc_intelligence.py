class IOCIntelligence:
    """
    IOC enrichment and intelligence analysis layer.
    """

    def analyze(self, indicators):

        results = []

        for indicator in indicators:

            results.append(
                {
                    "indicator": indicator,
                    "type": self.detect_type(indicator),
                    "confidence": 0.8,
                    "reputation": "unknown"
                }
            )

        return results


    def detect_type(self, indicator):

        if "." in indicator:
            return "domain"

        if "/" in indicator:
            return "url"

        return "unknown"