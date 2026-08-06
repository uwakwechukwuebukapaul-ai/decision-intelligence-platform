class TechniqueMapper:

    def map(self, indicator):

        indicator = indicator.lower()

        if indicator.endswith(".xyz"):

            return {
                "technique": "T1583.001",
                "name": "Acquire Infrastructure: Domains",
                "confidence": 0.90,
            }

        if indicator.endswith(".ru"):

            return {
                "technique": "T1583.001",
                "name": "Acquire Infrastructure: Domains",
                "confidence": 0.88,
            }

        return {
            "technique": "T1595",
            "name": "Active Scanning",
            "confidence": 0.70,
        }