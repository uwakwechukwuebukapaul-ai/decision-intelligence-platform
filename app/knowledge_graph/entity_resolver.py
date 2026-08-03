from datetime import datetime


class EntityResolver:

    def resolve(self, incident):

        entities = []

        keywords = incident.lower()

        if "ransomware" in keywords:
            entities.append({
                "type": "Malware",
                "value": "Ransomware"
            })

        if "powershell" in keywords:
            entities.append({
                "type": "Technique",
                "value": "T1059.001 PowerShell"
            })

        if "server" in keywords:
            entities.append({
                "type": "Asset",
                "value": "Server Infrastructure"
            })

        return {
            "entities": entities,
            "timestamp": datetime.utcnow().isoformat()
        }["entities"]