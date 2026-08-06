"""
Sentinel DNA Investigation Memory Engine
"""


from .memory_store import MemoryStore
from .memory_query import MemoryQuery
from .memory_schema import InvestigationMemoryRecord



class InvestigationMemory:


    def __init__(self):

        self.store = MemoryStore()

        self.query = MemoryQuery(
            self.store
        )



    def remember(
        self,
        intelligence: dict,
        decision: dict,
    ):

        record = InvestigationMemoryRecord(

            indicator=intelligence.get(
                "indicator",
                "unknown",
            ),

            risk_score=intelligence.get(
                "risk",
                {}
            ).get(
                "score",
                0,
            ),

            severity=intelligence.get(
                "risk",
                {}
            ).get(
                "risk",
                "unknown",
            ),

            decision=decision.get(
                "decision",
                "unknown",
            ),

            confidence=decision.get(
                "confidence",
                0,
            ),

            mitre_mapping=intelligence.get(
                "mitre_mapping",
                [],
            ),

            evidence=intelligence,

        )


        return self.store.save(
            record
        ).to_dict()



    def recall(
        self,
        indicator,
    ):

        return self.query.search_indicator(
            indicator
        )