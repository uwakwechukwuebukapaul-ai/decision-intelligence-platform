from datetime import datetime
import uuid


class EntityManager:


    def extract(self, event):

        entities = []


        if "powershell" in event.lower():

            entities.append({

                "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                "type": "Technique",
                "value": "PowerShell"

            })


        if "ransomware" in event.lower():

            entities.append({

                "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                "type": "Malware",
                "value": "Ransomware"

            })


        entities.append({

            "id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
            "type": "Asset",
            "value": "Enterprise Server"

        })


        return {

            "entities": entities,
            "timestamp": datetime.utcnow().isoformat()

        }