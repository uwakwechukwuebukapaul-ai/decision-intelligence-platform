from app.ai.persistent_intelligence.knowledge_repository import KnowledgeRepository


class KnowledgeRetriever:


    def __init__(self):

        self.repository = KnowledgeRepository()



    def search_knowledge(
        self,
        query
    ):

        result = self.repository.search(
            query
        )


        return {

            "query": query,

            "knowledge": result,

            "status": "completed"

        }