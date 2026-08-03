from datetime import datetime


class MITREDetectorMapper:

    def map(self, event):

        return {
            "techniques": [
                {
                    "id": "T1059.001",
                    "name": "PowerShell"
                },
                {
                    "id": "T1486",
                    "name": "Data Encrypted for Impact"
                }
            ],
            "framework": "MITRE ATT&CK",
            "timestamp": datetime.utcnow().isoformat()
        }