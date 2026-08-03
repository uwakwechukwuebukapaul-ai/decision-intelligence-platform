from datetime import datetime

from .entity_extractor import EntityExtractor
from .relationship_engine import RelationshipEngine
from .threat_knowledge import ThreatKnowledge
from .decision_knowledge import DecisionKnowledge
from .knowledge_memory import KnowledgeMemory



class KnowledgeGraph:
    """
    Sentinel DNA Enterprise Knowledge Graph Engine.
    """

    def __init__(self):

        self.extractor = EntityExtractor()
        self.relationship = RelationshipEngine()
        self.threat = ThreatKnowledge()
        self.decision = DecisionKnowledge()
        self.memory = KnowledgeMemory()



    def analyze(self, intelligence):


        entities_result = (
            self.extractor.extract(
                intelligence
            )
        )


        relationships = (
            self.relationship.connect(
                entities_result["entities"]
            )
        )


        threats = (
            self.threat.analyze(
                entities_result["entities"]
            )
        )


        decision = (
            self.decision.recommend(
                threats
            )
        )


        result = {

            "status":
                "completed",

            "knowledge_graph":

            {

                "input":
                    intelligence,


                "entities":
                    entities_result,


                "relationships":
                    relationships,


                "threat_intelligence":
                    threats,


                "decision":
                    decision

            },


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(result)


        return result