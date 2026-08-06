import uuid
from datetime import datetime


class EntityManager:


    def create_entity(self, name, entity_type):


        return {

            "entity_id":
            "ENT-" + uuid.uuid4().hex[:8].upper(),


            "name":
            name,


            "type":
            entity_type,


            "created_at":
            datetime.utcnow().isoformat(),

            "status":
            "registered"

        }