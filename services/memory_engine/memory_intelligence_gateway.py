"""
Sentinel DNA Memory Intelligence Gateway.

Unified access layer for security memory systems.

Responsibilities:

- Coordinate incident memory retrieval
- Coordinate pattern memory retrieval
- Coordinate knowledge memory retrieval
- Provide investigation context recall
- Prepare memory intelligence for AI agents

Architecture position:

AI Investigation Agents
          |
          v
Memory Intelligence Gateway
          |
+---------+----------+----------+
|                    |          |
IncidentMemory   PatternMemory  KnowledgeMemory
          |
          v
Persistent Memory Store
"""


class MemoryIntelligenceGateway:
    """
    Unified enterprise memory retrieval interface.

    Provides a single entry point for:

    - Previous incident recall
    - Threat pattern recall
    - Security knowledge recall
    - Investigation memory context
    """

    def __init__(
        self,
        incident_memory=None,
        pattern_memory=None,
        knowledge_memory=None,
        retrieval_engine=None
    ):

        self.incident_memory = incident_memory

        self.pattern_memory = pattern_memory

        self.knowledge_memory = knowledge_memory

        self.retrieval_engine = retrieval_engine



    def recall_incidents(
        self,
        query
    ):
        """
        Retrieve similar historical incidents.
        """

        if self.incident_memory:

            return self.incident_memory.find_similar(
                query
            )

        return []



    def recall_patterns(
        self,
        query
    ):
        """
        Retrieve learned attack patterns.
        """

        if self.pattern_memory:

            return self.pattern_memory.detect_pattern(
                query
            )

        return []



    def recall_knowledge(
        self,
        query
    ):
        """
        Retrieve security knowledge.
        """

        if self.knowledge_memory:

            return self.knowledge_memory.query(
                query
            )

        return []



    def retrieve(
        self,
        query
    ):
        """
        Unified memory retrieval.

        Combines:

        - Incident history
        - Attack patterns
        - Security knowledge
        """

        return {

            "query":
                query,


            "incidents":
                self.recall_incidents(
                    query
                ),


            "patterns":
                self.recall_patterns(
                    query
                ),


            "knowledge":
                self.recall_knowledge(
                    query
                ),


            "status":
                "completed"

        }



    def investigation_context(
        self,
        event
    ):
        """
        Build memory context for investigations.

        Used by:

        - Investigation Runtime
        - Cognitive Investigation Engine
        - Sentinel Copilot
        """

        query = str(
            event
        )


        memory = self.retrieve(
            query
        )


        return {

            "event":
                event,


            "memory_context":
                memory,


            "historical_matches":
                len(
                    memory.get(
                        "incidents",
                        []
                    )
                ),


            "pattern_matches":
                len(
                    memory.get(
                        "patterns",
                        []
                    )
                ),


            "knowledge_matches":
                len(
                    memory.get(
                        "knowledge",
                        []
                    )
                )

        }



    def health(
        self
    ):
        """
        Memory subsystem health status.
        """

        return {

            "service":
                "Memory Intelligence Gateway",


            "incident_memory":
                self.incident_memory is not None,


            "pattern_memory":
                self.pattern_memory is not None,


            "knowledge_memory":
                self.knowledge_memory is not None,


            "retrieval_engine":
                self.retrieval_engine is not None,


            "status":
                "healthy"

        }