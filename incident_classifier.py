from datetime import datetime


class IncidentClassifier:

    def classify(self, incident):

        severity = "critical" if (
            "ransomware" in incident.lower()
            or "breach" in incident.lower()
        ) else "medium"

        return {
            "incident_type": "Cyber Security Incident",
            "category": "Malware Activity",
            "severity": severity,
            "timestamp": datetime.utcnow().isoformat()
        }