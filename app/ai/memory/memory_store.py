from app.database.db import SessionLocal
from app.models.agent_memory import AgentMemory


class MemoryStore:


    def save_memory(
        self,
        agent_id,
        content,
        mission_id=None,
        memory_type="experience"
    ):

        db = SessionLocal()

        try:

            memory = AgentMemory(

                agent_id=agent_id,

                mission_id=mission_id,

                memory_type=memory_type,

                content=content

            )


            db.add(memory)

            db.commit()

            db.refresh(memory)


            return self.serialize(memory)


        finally:

            db.close()



    def get_memories(
        self,
        agent_id
    ):

        db = SessionLocal()

        try:

            memories = (

                db.query(AgentMemory)

                .filter(
                    AgentMemory.agent_id == agent_id
                )

                .order_by(
                    AgentMemory.created_at.desc()
                )

                .all()

            )


            return [

                self.serialize(memory)

                for memory in memories

            ]


        finally:

            db.close()



    def serialize(
        self,
        memory
    ):

        return {

            "id":
                memory.id,

            "agent_id":
                memory.agent_id,

            "mission_id":
                memory.mission_id,

            "memory_type":
                memory.memory_type,

            "content":
                memory.content,

            "created_at":
                memory.created_at.isoformat()

        }