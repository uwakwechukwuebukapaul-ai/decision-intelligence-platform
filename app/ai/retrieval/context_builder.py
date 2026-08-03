from app.ai.retrieval.knowledge_retriever import KnowledgeRetriever
from app.ai.retrieval.decision_history import DecisionHistory


class ContextBuilder:


    def __init__(self):

        self.knowledge = KnowledgeRetriever()

        self.history = DecisionHistory()



    def build_context(
        self,
        agent_id,
        mission
    ):


        knowledge = self.knowledge.search_knowledge(
            mission
        )


        return {

            "agent_id": agent_id,

            "mission": mission,

            "knowledge": knowledge,

            "decisions": self.history.get_history(),

            "context_ready": True

        }