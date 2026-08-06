class IOCEnrichment:

    def enrich(self, ioc):

        tags = []
        category = "unknown"
        reputation = "unknown"

        if "." in ioc:
            category = "domain"

        suspicious_terms = [
            "malware",
            "evil",
            "phishing",
            "c2",
            "bot"
        ]

        for term in suspicious_terms:
            if term in ioc.lower():
                tags.append(term)

        if tags:
            reputation = "malicious"
        else:
            reputation = "clean"

        return {
            "ioc": ioc,
            "category": category,
            "tags": tags,
            "reputation": reputation,
            "details": {
                "analysis": "IOC enrichment completed"
            }
        }