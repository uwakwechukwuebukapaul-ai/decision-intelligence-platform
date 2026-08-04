class SigmaMapper:

    def map(self, patterns):

        mappings = []

        for pattern in patterns:

            mappings.append(
                {
                    "framework": "Sigma",
                    "mapping": pattern
                }
            )

        return mappings