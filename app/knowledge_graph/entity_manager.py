from datetime import datetime
import uuid


class EntityManager:

    def extract(self, event):

        entities = []

        keywords = {
            "ransomware": "Malware",
            "powershell": "Execution Technique",
            "database": "Asset",
            "finance": "Organization",
            "server": "Infrastructure"
        }

        lower_event = event.lower()

        for keyword, entity_type in keywords.items():

            if keyword in lower_event:

                entities.append(
                    {
                        "entity_id": f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                        "name": keyword,
                        "type": entity_type
                    }
                )

        return {
            "entities": entities,
            "timestamp": datetime.utcnow().isoformat()
        }