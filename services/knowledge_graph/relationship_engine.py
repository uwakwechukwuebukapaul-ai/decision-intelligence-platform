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


        self.store.relationships.append(
            relationship
        )


        return relationship