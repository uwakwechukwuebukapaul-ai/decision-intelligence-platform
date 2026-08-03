from app.ai.knowledge_graph.graph_engine import GraphEngine


class KnowledgeContext:

    def __init__(self):
        self.graph = GraphEngine()


    def build_context(
        self,
        agent_id,
        mission
    ):

        agent = self.graph.add_node(
            "agent",
            agent_id
        )

        mission_node = self.graph.add_node(
            "mission",
            mission
        )


        self.graph.add_relationship(
            agent["node_id"],
            mission_node["node_id"],
            "assigned_to"
        )


        return {

            "agent": agent,

            "mission": mission_node,

            "knowledge":
                self.graph.get_graph()

        }