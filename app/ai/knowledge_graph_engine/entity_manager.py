from datetime import datetime


class EntityManager:
    """
    Knowledge Graph Entity Management Layer

    Maintains intelligence objects:
    - decisions
    - outcomes
    - strategies
    - lessons
    - patterns
    """


    def __init__(self):

        self.version = "1.0"

        self.entities = []



    def create_entity(
        self,
        entity_type,
        name,
        attributes=None
    ):


        entity = {

            "id":
                len(self.entities) + 1,


            "type":
                entity_type,


            "name":
                name,


            "attributes":
                attributes or {},


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.entities.append(entity)


        return entity



    def get_entities(self):

        return self.entities



entity_manager = EntityManager()