from datetime import datetime

from .node_manager import NodeManager
from .relationship_engine import RelationshipEngine
from .entity_resolver import EntityResolver
from .attack_mapper import AttackMapper
from .campaign_graph import CampaignGraph
from .graph_analyzer import GraphAnalyzer
from .graph_memory import GraphMemory



class ThreatGraphEngine:


    def __init__(self):

        self.nodes = NodeManager()
        self.relationships = RelationshipEngine()
        self.entities = EntityResolver()
        self.attack = AttackMapper()
        self.campaign = CampaignGraph()
        self.analyzer = GraphAnalyzer()
        self.memory = GraphMemory()



    def analyze(self, event):


        resolved = self.entities.resolve(event)


        created_nodes = []


        for entity in resolved["entities"]:

            node = self.nodes.create_node(
                entity["entity"],
                entity["type"]
            )

            created_nodes.append(node)



        edges = []


        if len(created_nodes) >= 2:


            for index in range(len(created_nodes)-1):

                edge = self.relationships.connect(
                    created_nodes[index]["name"],
                    created_nodes[index+1]["name"],
                    "associated_with"
                )

                edges.append(edge)



        mitre = self.attack.map(event)


        campaign = self.campaign.build(event)



        analysis = self.analyzer.analyze(
            created_nodes,
            edges
        )


        result = {

            "status": "completed",

            "event": event,

            "nodes": created_nodes,

            "relationships": edges,

            "mitre": mitre,

            "campaign": campaign,

            "analysis": analysis,

            "created_at":
                datetime.utcnow().isoformat()
        }


        self.memory.store(result)


        return result