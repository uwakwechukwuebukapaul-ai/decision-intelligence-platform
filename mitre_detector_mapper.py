from datetime import datetime


class MITREDetectorMapper:

    def map(self, threat):

        return {

            "framework":
                "MITRE ATT&CK",

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

            "timestamp":
                datetime.utcnow().isoformat()
        }