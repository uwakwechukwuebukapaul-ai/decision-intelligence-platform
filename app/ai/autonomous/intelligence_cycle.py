from datetime import datetime

from app.ai.memory_integration.memory_manager import MemoryManager
from app.ai.learning.learning_engine import LearningEngine
from app.ai.self_improvement.improvement_loop import ImprovementLoop
from app.ai.evolution.evolution_engine import EvolutionEngine



class IntelligenceCycle:


    def __init__(self):

        self.memory = MemoryManager()

        self.learning = LearningEngine()

        self.improvement = ImprovementLoop()

        self.evolution = EvolutionEngine()



    def run(

        self,

        agent_id,

        mission_id,

        execution_results

    ):


        memories = []


        for result in execution_results:


            memory = self.memory.store_experience(

                agent_id,

                mission_id,

                result.get(
                    "output",
                    ""
                )

            )


            memories.append(memory)



        learning_result = self.learning.learn(

            agent_id

        )



        improvement_result = self.improvement.improve(

            agent_id,

            execution_results

        )



        evolution_result = self.evolution.evolve(

            {
                "name":
                    agent_id
            },

            learning_result

        )



        return {

            "agent_id":
                agent_id,

            "mission_id":
                mission_id,

            "memories_created":
                len(memories),

            "learning":
                learning_result,

            "improvement":
                improvement_result,

            "evolution":
                evolution_result,

            "status":
                "completed",

            "timestamp":
                datetime.utcnow().isoformat()

        }