class GraphRepository:


    def __init__(self):

        self.entities = []

        self.relationships = []



    def save_entity(self, entity):

        self.entities.append(entity)

        return entity



    def save_relationship(self, relationship):

        self.relationships.append(relationship)

        return relationship



    def get_entities(self):

        return self.entities



    def get_relationships(self):

        return self.relationships