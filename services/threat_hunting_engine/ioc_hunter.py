class IOCHunter:
    """
    IOC search and enrichment component.
    """

    def hunt(self, indicators):
        results = []

        if not indicators:
            return results

        for indicator in indicators:

            results.append(
                {
                    "indicator": indicator,
                    "status": "analyzed",
                    "risk": self.calculate_risk(indicator),
                }
            )

        return results

    def calculate_risk(self, indicator):

        suspicious_terms = [
            "malware",
            "evil",
            "payload",
            "phishing",
            "ransom",
        ]

        value = str(indicator).lower()

        for term in suspicious_terms:
            if term in value:
                return "HIGH"

        return "LOW"