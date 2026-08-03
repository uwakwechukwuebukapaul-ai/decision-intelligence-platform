from datetime import datetime
import uuid


class EntityCorrelator:


    def correlate(self, event):

        entities = []


        text = event["original_event"].lower()


        if "powershell" in text:
            entities.append({
                "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                "type": "Technique",
                "value": "PowerShell"
            })


        if "ransomware" in text:
            entities.append({
                "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                "type": "Malware",
                "value": "Ransomware"
            })


        if "server" in text:
            entities.append({
                "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                "type": "Asset",
                "value": "Server Infrastructure"
            })


        return {
            "entities": entities,
            "timestamp": datetime.utcnow().isoformat()
        }