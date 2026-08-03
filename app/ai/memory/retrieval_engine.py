from app.ai.memory.memory_store import MemoryStore


class RetrievalEngine:


    def __init__(self):

        self.memory_store = MemoryStore()



    def retrieve_context(
        self,
        agent_id,
        keyword=None
    ):

        memories = self.memory_store.get_memories(
            agent_id
        )


        if keyword:

            keyword = keyword.lower()

            memories = [

                memory

                for memory in memories

                if keyword in memory["content"].lower()

            ]


        return {

            "agent_id":
                agent_id,

            "memory_count":
                len(memories),

            "memories":
                memories

        }