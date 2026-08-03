from .security_entity import SecurityEntity


class EntityManager:

    def __init__(self):
        self.entities = []
        self.creator = SecurityEntity()

    def extract(self, event):

        entities = []

        keywords = {
            "ransomware": "Malware",
            "powershell": "Technique",
            "finance": "Business Asset",
            "server": "Infrastructure",
            "actor": "Threat Actor",
            "database": "Data Asset"
        }

        text = event.lower()

        for keyword, entity_type in keywords.items():

            if keyword in text:

                entity = self.creator.create(
                    keyword,
                    entity_type,
                    "high"
                )

                self.entities.append(entity)
                entities.append(entity)

        return {
            "entities": entities,
            "count": len(entities)
        }

    def get_entities(self):

        return self.entities