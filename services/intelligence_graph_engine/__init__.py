from .graph_engine import IntelligenceGraphEngine
from .node_manager import NodeManager
from .relationship_engine import RelationshipEngine
from .entity_resolver import EntityResolver
from .knowledge_mapper import KnowledgeMapper
from .graph_reasoner import GraphReasoner
from .graph_memory import GraphMemory
from .graph_orchestrator import GraphOrchestrator


class IntelligenceGraphPlatform:
    """
    Sentinel DNA Intelligence Graph Platform.

    Unified reasoning graph connecting:
    - Threat Intelligence
    - Cases
    - Evidence
    - IOCs
    - Threat Actors
    - Malware
    - Vulnerabilities
    - MITRE ATT&CK knowledge
    """

    def __init__(self):

        self.graph_engine = IntelligenceGraphEngine()
        self.node_manager = NodeManager()
        self.relationship_engine = RelationshipEngine()
        self.entity_resolver = EntityResolver()
        self.knowledge_mapper = KnowledgeMapper()
        self.graph_reasoner = GraphReasoner()
        self.graph_memory = GraphMemory()
        self.orchestrator = GraphOrchestrator()


    def status(self):

        return {
            "platform": "Sentinel DNA Intelligence Graph",
            "status": "operational"
        }