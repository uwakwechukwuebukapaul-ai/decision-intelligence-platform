from uuid import uuid4

from .memory_schema import InvestigationMemory
from .memory_repository import MemoryRepository
from .pattern_analyzer import PatternAnalyzer



class MemoryEngine:


    def __init__(self):

        self.repository = MemoryRepository()

        self.pattern_analyzer = PatternAnalyzer()



    def remember(
        self,
        incident_id,
        indicator,
        decision,
        priority,
        confidence
    ):

        history = self.repository.find_by_indicator(
            indicator
        )


        patterns = self.pattern_analyzer.analyze(
            indicator,
            history
        )


        memory = InvestigationMemory(

            memory_id=f"MEM-{str(uuid4())[:8].upper()}",

            incident_id=incident_id,

            indicator=indicator,

            decision=decision,

            priority=priority,

            confidence=confidence,

            patterns=patterns

        )


        return self.repository.save(memory).__dict__



    def recall(self, indicator):

        return [

            item.__dict__

            for item in self.repository.find_by_indicator(
                indicator
            )

        ]