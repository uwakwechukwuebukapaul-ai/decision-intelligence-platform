from datetime import datetime
import uuid


class EntityScoring:


    def evaluate(self, event):

        entities = []

        if "server" in event.lower():
            entities.append(
                {
                    "id":
                    f"ENTITY-{uuid.uuid4().hex[:6].upper()}",
                    "type":
                    "Asset",
                    "value":
                    "Server Infrastructure",
                    "risk":
                    95
                }
            )


        return {

            "entities": entities,

            "timestamp":
                datetime.utcnow().isoformat()

        }