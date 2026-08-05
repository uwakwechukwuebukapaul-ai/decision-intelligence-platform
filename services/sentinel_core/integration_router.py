"""
Sentinel DNA Core Integration Router.

Central intelligence routing layer connecting:
- Threat Intelligence
- MITRE Mapping
- Detection Engineering
- Knowledge Graph
- Attack Reasoning
- Memory Engine
"""


from services.threat_intelligence import ThreatIntelligenceEngine
from services.mitre_engine import MitreEngine
from services.detection_engine import DetectionEngine
from services.knowledge_graph import KnowledgeGraphEngine
from services.attack_reasoning import AttackReasoningEngine
from services.intelligence_memory import IntelligenceMemoryEngine



class IntegrationRouter:
    """
    Routes security events through Sentinel DNA intelligence layers.
    """



    def __init__(self):

        self.threat_intelligence = ThreatIntelligenceEngine()

        self.mitre = MitreEngine()

        self.detection = DetectionEngine()

        self.graph = KnowledgeGraphEngine()

        self.attack_reasoning = AttackReasoningEngine()

        self.memory = IntelligenceMemoryEngine()



    def collect(
        self,
        event
    ):
        """
        Execute complete intelligence collection pipeline.
        """


        threat_intelligence = self.threat_intelligence.analyze(
            event
        )


        mitre_analysis = self.mitre.map(
            event
        )


        detection_analysis = self.detection.detect(
            event
        )


        knowledge_graph = self.graph.process(
            event
        )


        attack_reasoning = self.attack_reasoning.process(
            knowledge_graph
        )


        memory_result = self.memory.remember(
            event
        )



        return {


            "threat_intelligence":

                threat_intelligence,


            "mitre":

                mitre_analysis,


            "detection":

                detection_analysis,


            "knowledge_graph":

                knowledge_graph,


            "attack_reasoning":

                attack_reasoning,


            "memory":

                memory_result

        }