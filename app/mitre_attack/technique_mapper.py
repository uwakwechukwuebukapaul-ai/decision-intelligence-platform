from datetime import datetime


class TechniqueMapper:

    def map(self, event):

        techniques = []

        event_lower = event.lower()

        if "powershell" in event_lower:
            techniques.append(
                {
                    "id": "T1059.001",
                    "name": "PowerShell"
                }
            )

        if "ransomware" in event_lower or "encryption" in event_lower:
            techniques.append(
                {
                    "id": "T1486",
                    "name": "Data Encrypted for Impact"
                }
            )

        if "credential" in event_lower:
            techniques.append(
                {
                    "id": "T1003",
                    "name": "OS Credential Dumping"
                }
            )

        if not techniques:
            techniques.append(
                {
                    "id": "T0000",
                    "name": "Unknown Technique"
                }
            )

        return {
            "techniques": techniques,
            "timestamp": datetime.utcnow().isoformat()
        }