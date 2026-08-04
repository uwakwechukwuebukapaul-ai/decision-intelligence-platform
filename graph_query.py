class GraphQuery:


    def find_entity(
        self,
        store,
        entity_id
    ):

        return store.nodes.get(entity_id)



    def find_relationships(
        self,
        store,
        entity_id
    ):

        return [

            edge for edge in store.edges

            if edge["source"] == entity_id

            or edge["target"] == entity_id

        ]