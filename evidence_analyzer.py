from datetime import datetime


class EvidenceAnalyzer:

    def analyze(self, evidence):

        event = evidence.get(
            "raw_event",
            ""
        ).lower()


        findings = []

        if "powershell" in event:
            findings.append(
                "Command Execution Detected"
            )

        if "ransomware" in event:
            findings.append(
                "Encryption Behavior Detected"
            )


        return {
            "findings": findings,
            "risk_score": 100 if findings else 20,
            "timestamp": datetime.utcnow().isoformat()
        }