class EvidenceAnalyzer:
    """
    Analyze security evidence collected from Sentinel DNA data sources.
    """

    def analyze(self, evidence):

        findings = []

        if evidence.get("ip"):
            findings.append(
                "Network indicator identified"
            )

        if evidence.get("domain"):
            findings.append(
                "Suspicious domain detected"
            )

        if evidence.get("hash"):
            findings.append(
                "File hash requires reputation lookup"
            )

        return {
            "findings": findings,
            "evidence_count": len(findings)
        }