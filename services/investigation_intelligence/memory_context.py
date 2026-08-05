from services.memory_engine.memory_retrieval import MemoryRetrieval
from services.memory_engine.incident_memory import IncidentMemory
from services.memory_engine.pattern_memory import PatternMemory


class MemoryContext:
    """
    Sentinel DNA Investigation Memory Context.

    Provides historical intelligence
    before investigation reasoning.

    Memory sources:

    - Previous investigations
    - Incident outcomes
    - Threat patterns
    - Security knowledge
    """


    def __init__(
        self,
        store=None
    ):

        self.store = store


        self.retrieval = None


        if store:

            self.retrieval = MemoryRetrieval(
                store
            )


        self.incidents = IncidentMemory(
            store
        )


        self.patterns = PatternMemory(
            store
        )



    def retrieve(
        self,
        event
    ):
        """
        Retrieve historical intelligence
        related to an incoming investigation.
        """


        query = str(
            event
        )


        memories = []


        if self.retrieval:

            memories = self.retrieval.recall(
                query
            )


        incidents = self.incidents.find_similar(
            query
        )


        patterns = self.patterns.detect_pattern(
            query
        )


        return {

            "query":
                query,


            "previous_memories":
                memories,


            "similar_incidents":
                incidents,


            "known_patterns":
                patterns,


            "memory_available":
                True

        }



    def store_incident(
        self,
        incident
    ):
        """
        Store completed investigation
        for future reasoning.
        """


        return self.incidents.remember(
            incident
        )



    def store_pattern(
        self,
        pattern
    ):
        """
        Store discovered attack pattern.
        """


        return self.patterns.learn(
            pattern
        )