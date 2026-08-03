from app.ai.collaboration.collaboration_engine import CollaborationEngine


class DecisionPipeline:


    def __init__(self):

        self.collaboration = CollaborationEngine()



    def run(
        self,
        mission_id,
        objective,
        agents
    ):


        analyses = []


        for agent in agents:

            analyses.append({

                "agent":
                    agent,

                "analysis":
                    f"{agent} analyzed: {objective}"

            })



        result = self.collaboration.execute_collaboration(

            mission_id,

            objective,

            agents,

            analyses

        )


        return result