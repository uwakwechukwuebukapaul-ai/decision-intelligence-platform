from datetime import datetime

from app.ai.memory.memory_engine import MemoryEngine



class MemoryManager:


    def __init__(self):

        self.memory_engine = MemoryEngine()



    def store_experience(
        self,
        agent_id,
        mission_id,
        experience
    ):

        memory = self.memory_engine.remember(

            agent_id=agent_id,

            mission_id=mission_id,

            content=experience

        )


        return {

            "status":
                "stored",

            "agent_id":
                agent_id,

            "mission_id":
                mission_id,

            "memory":
                memory,

            "timestamp":
                datetime.utcnow().isoformat()

        }



    def recall_agent_memory(
        self,
        agent_id,
        topic
    ):

        return self.memory_engine.recall(

            agent_id,

            topic

        )