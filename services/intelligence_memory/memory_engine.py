from .memory_store import MemoryStore
from .entity_memory import EntityMemory
from .threat_memory import ThreatMemory
from .case_memory import CaseMemory


class IntelligenceMemoryEngine:
    """
    Persistent intelligence memory layer.

    Stores:
    - Entities
    - Threat intelligence
    - Investigation cases
    - Fusion intelligence snapshots
    """


    def __init__(self):

        self.store = MemoryStore()


        self.entity_memory = EntityMemory(
            self.store
        )


        self.threat_memory = ThreatMemory(
            self.store
        )


        self.case_memory = CaseMemory(
            self.store
        )



    def remember_entity(
        self,
        entity_type,
        name,
        context=None
    ):

        return self.entity_memory.remember(
            entity_type,
            name,
            context
        )



    def remember_threat(
        self,
        name,
        techniques=None
    ):

        return self.threat_memory.remember(
            name,
            techniques
        )



    def remember_case(
        self,
        incident,
        resolution
    ):

        return self.case_memory.remember_case(
            incident,
            resolution
        )



    def remember_intelligence(
        self,
        intelligence
    ):
        """
        Stores intelligence fusion output.
        """

        snapshot = {

            "event":
                intelligence.get(
                    "event"
                ),

            "classification":
                intelligence.get(
                    "classification",
                    "unknown"
                ),

            "risk_score":
                intelligence.get(
                    "risk_score",
                    0
                ),

            "confidence":
                intelligence.get(
                    "confidence",
                    0
                )

        }


        return self.store.store_intelligence(
            snapshot
        )



    def remember(
        self,
        event
    ):
        """
        Backward compatibility adapter.
        """

        return self.threat_memory.remember(
            event,
            []
        )



    def recall(self):

        return {

            "entities":
                self.store.get_entities(),


            "threats":
                self.store.get_threats(),


            "cases":
                self.store.get_cases(),


            "intelligence":
                self.store.get_intelligence(),


            "status":
                "memory_active"

        }