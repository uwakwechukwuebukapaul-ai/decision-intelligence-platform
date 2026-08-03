from datetime import datetime
import uuid


class SecurityEntity:

    def create(
        self,
        name,
        entity_type,
        risk="unknown"
    ):

        return {
            "entity_id": f"ENTITY-{uuid.uuid4().hex[:8].upper()}",
            "name": name,
            "type": entity_type,
            "risk": risk,
            "created_at": datetime.utcnow().isoformat()
        }