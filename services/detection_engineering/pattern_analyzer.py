class PatternAnalyzer:
    """
    Analyze attacker behaviors and convert them into
    detection opportunities.
    """

    def analyze(self, events):

        patterns = []

        for event in events:

            if "powershell" in event.lower():
                patterns.append(
                    {
                        "technique": "T1059.001",
                        "pattern": "PowerShell execution"
                    }
                )

            if "credential" in event.lower():
                patterns.append(
                    {
                        "technique": "T1003",
                        "pattern": "Credential access behavior"
                    }
                )

        return patterns