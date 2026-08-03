from datetime import datetime


class SigmaGenerator:

    def generate(self, event):

        return {
            "sigma_rule": {
                "title": "Suspicious Ransomware Activity Detection",
                "logsource": "Endpoint Security",
                "detection": [
                    "PowerShell execution",
                    "File encryption behavior"
                ]
            },
            "timestamp": datetime.utcnow().isoformat()
        }