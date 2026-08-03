from datetime import datetime


class EvidenceReasoner:

    def analyze(self, incident):

        findings = []

        text = incident.lower()

        if "powershell" in text:
            findings.append(
                "PowerShell execution detected"
            )

        if "ransomware" in text:
            findings.append(
                "Encryption behavior identified"
            )

        findings.append(
            "Endpoint and security telemetry required"
        )

        return {
            "findings": findings,
            "confidence": "high",
            "timestamp": datetime.utcnow().isoformat()
        }