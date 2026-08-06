"""
Sentinel DNA Graph Query Layer
"""


class GraphQuery:


    def __init__(
        self,
        store,
    ):

        self.store = store



    def investigate_entity(
        self,
        entity_id: str,
    ):


        entity = self.store.get_entity(
            entity_id
        )


        relationships = (
            self.store.get_relationships(
                entity_id
            )
        )


        return {

            "entity": entity,

            "relationships": relationships,

            "relationship_count":
                len(relationships)

        }