from datetime import datetime
import uuid


class IOCManager:


    def extract(self, threat):

        indicators = []

        text = threat.lower()


        if "powershell" in text:
            indicators.append({
                "id": f"IOC-{uuid.uuid4().hex[:6].upper()}",
                "type": "Technique",
                "value": "PowerShell"
            })


        if "ransomware" in text:
            indicators.append({
                "id": f"IOC-{uuid.uuid4().hex[:6].upper()}",
                "type": "Malware",
                "value": "Ransomware"
            })


        return {
            "indicators": indicators,
            "timestamp": datetime.utcnow().isoformat()
        }