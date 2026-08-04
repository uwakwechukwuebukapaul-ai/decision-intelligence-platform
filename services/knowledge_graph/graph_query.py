class GraphQuery:


    def __init__(self, store):

        self.store = store



    def find_entities(self, entity_type):

        return [

            entity

            for entity in self.store.entities

            if entity["type"] == entity_type

        ]