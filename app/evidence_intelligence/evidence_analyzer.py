from datetime import datetime


class EvidenceAnalyzer:

    def analyze(self, evidence):

        text = str(evidence).lower()

        findings = []

        if "powershell" in text:
            findings.append(
                "Suspicious command execution detected"
            )

        if "ransomware" in text:
            findings.append(
                "Encryption based malware behavior detected"
            )

        if "database" in text:
            findings.append(
                "Critical asset targeting detected"
            )

        return {
            "findings": findings,
            "risk_score": 100
            if "ransomware" in text
            else 50,
            "analysis_status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        }