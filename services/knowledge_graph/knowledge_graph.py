from .entity import Entity


class KnowledgeGraph:
    """
    Sentinel DNA Knowledge Graph Engine.

    Responsibilities:
    - Store security entities
    - Track relationships
    - Process investigation events
    - Provide graph intelligence
    - Maintain backward compatibility
    """

    def __init__(self):

        self.entities = {}
        self.relationships = []


    def add_entity(self, entity: Entity):
        """
        Add entity into knowledge graph.
        """

        self.entities[entity.name] = entity

        return entity.to_dict()



    def add_relationship(
        self,
        source,
        relation,
        target
    ):
        """
        Create relationship between entities.
        """

        relationship = {

            "source": source,
            "relation": relation,
            "target": target

        }


        self.relationships.append(
            relationship
        )


        return relationship



    def get_relationships(self):

        return self.relationships



    def find_entity(
        self,
        name
    ):

        return self.entities.get(name)



    def process(
        self,
        event
    ):
        """
        Compatibility pipeline method.

        Converts security events into
        graph intelligence.

        Used by:
        services.sentinel_core.integration_router
        """

        normalized = event.lower()


        entity_patterns = {

            "ransomware": "Ransomware",
            "powershell": "PowerShell",
            "database": "Database",
            "server": "Server",
            "finance": "Finance",
            "malware": "Malware",
            "credential": "Credential Access"

        }


        detected_entities = []


        for keyword, entity_name in entity_patterns.items():

            if keyword in normalized:


                entity = Entity(

                    name=entity_name,

                    entity_type="security_entity"

                )


                self.add_entity(
                    entity
                )


                detected_entities.append(
                    entity_name
                )



        # Build relationships automatically

        for source in detected_entities:

            for target in detected_entities:

                if source != target:

                    self.add_relationship(

                        source,

                        "associated_with",

                        target

                    )



        return {

            "status": "knowledge_graph_processed",

            "event": event,

            "entities": detected_entities,

            "graph": self.export()

        }



    def analyze(
        self,
        event
    ):
        """
        Higher-level graph analysis interface.
        """

        result = self.process(
            event
        )


        result["status"] = "knowledge_graph_analyzed"


        return result



    def export(self):

        return {

            "entities":
            [

                entity.to_dict()

                for entity in self.entities.values()

            ],

            "relationships":

            self.relationships

        }