class CoverageAnalyzer:
    """
    MITRE ATT&CK detection coverage analyzer.
    """

    def analyze(self, techniques):

        return {
            "covered_techniques": techniques,
            "coverage_count": len(techniques),
            "coverage_score":
                min(len(techniques) * 10, 100)
        }