from datetime import datetime


class SignalCorrelator:
    """
    Correlates security signals across Sentinel DNA modules.
    """

    def correlate(self, signals):

        findings = []

        text = str(signals).lower()

        indicators = [
            "ransomware",
            "malware",
            "phishing",
            "powershell",
            "credential"
        ]

        for indicator in indicators:
            if indicator in text:
                findings.append(indicator)

        return {
            "correlated_signals": findings,
            "count": len(findings),
            "timestamp": datetime.utcnow().isoformat()
        }