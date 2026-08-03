from app.ai.retrieval.retrieval_engine import RetrievalEngine


class BrainRetrievalConnector:


    def __init__(self):

        self.retrieval_engine = RetrievalEngine()



    def retrieve_context(
        self,
        agent_id,
        mission
    ):

        return self.retrieval_engine.retrieve(
            agent_id,
            mission
        )