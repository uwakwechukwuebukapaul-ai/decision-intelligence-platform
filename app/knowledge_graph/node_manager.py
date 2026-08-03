from datetime import datetime
import uuid


class NodeManager:

    def create_nodes(self, incident, entities):

        return {
            "nodes": [
                {
                    "id": f"NODE-{uuid.uuid4().hex[:8].upper()}",
                    "type": entity["type"],
                    "value": entity["value"]
                }
                for entity in entities
            ],
            "incident": incident,
            "created_at": datetime.utcnow().isoformat()
        }