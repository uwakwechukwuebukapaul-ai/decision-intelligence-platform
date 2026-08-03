from datetime import datetime


class AnomalyDetector:

    def detect(self, threat):

        findings = []

        text = threat.lower()

        if "ransomware" in text:
            findings.append(
                "Mass encryption behavior detected"
            )

        if "powershell" in text:
            findings.append(
                "Suspicious command execution detected"
            )

        if not findings:
            findings.append(
                "No major anomaly detected"
            )

        return {
            "findings": findings,
            "risk": "critical" if len(findings) > 1 else "medium",
            "timestamp": datetime.utcnow().isoformat()
        }