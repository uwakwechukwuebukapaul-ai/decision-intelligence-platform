from datetime import datetime


class ThreatReasoner:

    def analyze(self, incident):

        techniques = []

        text = incident.lower()

        if "powershell" in text:
            techniques.append(
                {
                    "id": "T1059.001",
                    "name": "PowerShell"
                }
            )

        if "ransomware" in text:
            techniques.append(
                {
                    "id": "T1486",
                    "name": "Data Encrypted for Impact"
                }
            )

        return {
            "framework": "MITRE ATT&CK",
            "techniques": techniques,
            "timestamp": datetime.utcnow().isoformat()
        }