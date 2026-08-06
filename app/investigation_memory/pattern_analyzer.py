class PatternAnalyzer:


    def analyze(self, indicator, history):

        patterns = []


        if len(history) > 0:

            patterns.append(
                "Recurring threat indicator detected"
            )


        if indicator.endswith(".xyz"):

            patterns.append(
                "Suspicious domain pattern detected"
            )


        if not patterns:

            patterns.append(
                "No previous threat pattern identified"
            )


        return patterns