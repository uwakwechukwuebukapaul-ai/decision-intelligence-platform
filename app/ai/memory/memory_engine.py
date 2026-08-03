from app.ai.memory.memory_store import MemoryStore
from app.ai.memory.retrieval_engine import RetrievalEngine


class MemoryEngine:


    def __init__(self):

        self.store = MemoryStore()

        self.retriever = RetrievalEngine()



    def remember(
        self,
        agent_id,
        content,
        mission_id=None,
        memory_type="experience"
    ):

        return self.store.save_memory(

            agent_id=agent_id,

            mission_id=mission_id,

            content=content,

            memory_type=memory_type

        )



    def recall(
        self,
        agent_id,
        topic=None
    ):

        return self.retriever.retrieve_context(

            agent_id,

            topic

        )