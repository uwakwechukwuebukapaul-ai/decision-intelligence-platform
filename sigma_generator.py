from datetime import datetime


class SigmaGenerator:

    def generate(self, threat):

        return {
            "format": "Sigma",
            "title": "AI Generated Detection Rule",
            "detection": {
                "keywords": [
                    "powershell",
                    "ransomware",
                    "encryption"
                ]
            },
            "timestamp": datetime.utcnow().isoformat()
        }