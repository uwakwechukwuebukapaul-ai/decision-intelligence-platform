from datetime import datetime


class CaseAnalyzer:

    def analyze(self, incident):

        severity = "low"
        classification = "Suspicious Activity"

        keywords = incident.lower()

        if "ransomware" in keywords:
            severity = "critical"
            classification = "Ransomware Attack"

        elif "malware" in keywords:
            severity = "high"
            classification = "Malware Incident"

        elif "powershell" in keywords:
            severity = "high"
            classification = "Suspicious Execution"

        return {
            "classification": classification,
            "severity": severity,
            "timestamp": datetime.utcnow().isoformat()
        }