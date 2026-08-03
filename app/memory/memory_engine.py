from app.memory.memory_repository import (
    MemoryRepository
)

from app.memory.secure_memory import (
    SecureMemory
)

from app.memory.memory_audit import (
    MemoryAudit
)

from app.memory.decision_memory import (
    DecisionMemory
)

from app.memory.research_memory import (
    ResearchMemory
)

from app.memory.agent_memory import (
    AgentMemory
)

from app.memory.learning_memory import (
    LearningMemory
)



class MemoryEngine:


    def __init__(self):


        self.repository = MemoryRepository()


        self.security = SecureMemory()


        self.audit = MemoryAudit()



        self.decision = DecisionMemory(
            self.repository
        )


        self.research = ResearchMemory(
            self.repository
        )


        self.agent = AgentMemory(
            self.repository
        )


        self.learning = LearningMemory(
            self.repository
        )



    def store_secure(
        self,
        user,
        category,
        data
    ):


        protection = self.security.encrypt(
            data
        )


        record = {


            "data":
                data,


            "security_hash":
                protection["hash"]

        }



        result = self.repository.save(

            category,

            record

        )


        self.audit.record(

            user,

            "STORE",

            category

        )


        return result