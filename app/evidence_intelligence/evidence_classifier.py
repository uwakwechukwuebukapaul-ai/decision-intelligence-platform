from datetime import datetime


class EvidenceClassifier:

    def classify(self, evidence):

        text = str(evidence).lower()

        categories = []

        if "ransomware" in text:
            categories.append("Malware")

        if "powershell" in text:
            categories.append("Execution Technique")

        if "attack" in text:
            categories.append("Security Incident")

        if not categories:
            categories.append("Unknown Activity")

        return {
            "classification": categories,
            "severity": "critical"
            if "ransomware" in text
            else "medium",
            "timestamp": datetime.utcnow().isoformat()
        }