from app.ai.brain.agent_brain import AgentBrain
from app.ai.brain_integration.knowledge_context import KnowledgeContext


class BrainConnector:


    def __init__(self):

        self.brain = AgentBrain()

        self.knowledge = KnowledgeContext()



    def think_with_knowledge(
        self,
        agent_id,
        mission
    ):


        context = self.knowledge.build_context(
            agent_id,
            mission
        )


        result = self.brain.think(
            agent_id,
            mission,
            [
                context
            ]
        )


        return {

            "knowledge_context":
                context,

            "brain_result":
                result,

            "status":
                "completed"

        }