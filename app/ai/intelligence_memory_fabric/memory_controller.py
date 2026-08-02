from datetime import datetime


from .decision_memory import DecisionMemory
from .experience_memory import ExperienceMemory
from .knowledge_memory import KnowledgeMemory
from .learning_patterns import LearningPatterns
from .memory_state import MemoryState



class MemoryController:


    def __init__(self):

        self.decision_memory = DecisionMemory()

        self.experience_memory = ExperienceMemory()

        self.knowledge_memory = KnowledgeMemory()

        self.learning_patterns = LearningPatterns()

        self.memory_state = MemoryState()



    def generate_memory_state(self, user_id):


        return {


            "user_id": user_id,


            "memory_controller": {


                "status": "active",

                "memory_score": 99,

                "generated_at":
                    datetime.utcnow().isoformat(),

                "version": "1.0"

            },


            "decision_memory":

                self.decision_memory.get_decisions(),


            "experience_memory":

                self.experience_memory.get_experiences(),


            "knowledge_memory":

                self.knowledge_memory.get_knowledge(),


            "learning_patterns":

                self.learning_patterns.analyze_patterns(),


            "memory_state":

                self.memory_state.get_state(),


            "overall_memory_score": 99

        }