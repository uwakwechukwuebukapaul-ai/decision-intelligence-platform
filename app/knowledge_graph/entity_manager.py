class EntityManager:


    def __init__(self, graph):

        self.graph = graph


    def register_incident(self, incident):

        return self.graph.add_entity(
            "incident",
            incident["incident_id"],
            incident
        )


    def register_ioc(self, ioc):

        return self.graph.add_entity(
            "ioc",
            ioc["ioc"],
            ioc
        )