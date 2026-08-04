from services.threat_intelligence import ThreatIntelligenceEngine
from services.mitre_engine import MITREEngine
from services.detection_engine import DetectionEngine
from services.knowledge_graph import KnowledgeGraphEngine
from services.intelligence_memory import IntelligenceMemoryEngine


class IntegrationRouter:

    def __init__(self):

        self.threat_intelligence = ThreatIntelligenceEngine()
        self.mitre = MITREEngine()
        self.detection = DetectionEngine()
        self.graph = KnowledgeGraphEngine()
        self.memory = IntelligenceMemoryEngine()


    def collect(self, event):

        return {

            "threat_intelligence":
                self.threat_intelligence.analyze(event),

            "mitre":
                self.mitre.map(event),

            "detection":
                self.detection.detect(event),

            "knowledge_graph":
                self.graph.process(event),

            "memory":
                self.memory.remember(event)

        }