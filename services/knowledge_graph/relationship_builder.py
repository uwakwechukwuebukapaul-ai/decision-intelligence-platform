class RelationshipEngine:

    def __init__(self, store):

        self.store = store


    def create_relationship(
        self,
        source,
        relation,
        target
    ):

        relationship = {

            "source": source,

            "relation": relation,

            "target": target

        }

        self.store.add_relationship(
            relationship
        )

        return relationship


    def build(
        self,
        entities
    ):

        relationships = []

        if len(entities) >= 2:

            relationships.append(
                self.create_relationship(
                    entities[0],
                    "related_to",
                    entities[1]
                )
            )

        return relationships