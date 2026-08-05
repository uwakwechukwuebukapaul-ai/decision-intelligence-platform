class SignalCorrelator:

    def correlate(self, signals):

        relationships = []

        for signal in signals:

            relationships.append(
                {
                    "signal": signal,
                    "correlated": True
                }
            )

        return relationships


    def match_patterns(self, signals):

        return {
            "patterns_found": len(signals)
        }