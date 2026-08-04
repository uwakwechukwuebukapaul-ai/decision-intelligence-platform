from datetime import datetime


class EvidenceClassifier:

    def classify(self, evidence):

        event = evidence.get(
            "raw_event",
            ""
        ).lower()

        severity = "low"

        if "ransomware" in event:
            severity = "critical"

        elif "malware" in event:
            severity = "high"


        return {
            "classification": "Security Incident Evidence",
            "severity": severity,
            "timestamp": datetime.utcnow().isoformat()
        }