from app.ai.evolution.evolution_engine import EvolutionEngine



class EvolutionManager:


    def __init__(self):

        self.engine = EvolutionEngine()



    def evolve_agent(

        self,

        agent_id,

        learning_data

    ):


        return self.engine.evolve(

            {
                "name":
                    agent_id
            },

            learning_data

        )