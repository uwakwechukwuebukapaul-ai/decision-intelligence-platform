class EntityManager:


    def create_entity(
        self,
        entity_type,
        name
    ):

        return {

            "id": name.lower().replace(" ","_"),

            "type": entity_type,

            "name": name

        }