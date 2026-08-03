from datetime import datetime


class ThreatMapping:

    def map(self, threat):

        techniques = []

        text = threat.lower()

        if "powershell" in text:
            techniques.append(
                {
                    "technique": "Command and Scripting Interpreter",
                    "id": "T1059"
                }
            )

        if "ransomware" in text:
            techniques.append(
                {
                    "technique": "Data Encrypted for Impact",
                    "id": "T1486"
                }
            )

        return {
            "framework": "MITRE ATT&CK",
            "techniques": techniques,
            "count": len(techniques),
            "timestamp": datetime.utcnow().isoformat()
        }