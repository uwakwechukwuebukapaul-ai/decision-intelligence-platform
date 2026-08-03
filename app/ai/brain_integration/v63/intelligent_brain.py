from datetime import datetime

from app.ai.brain.reasoning_engine import ReasoningEngine
from app.ai.brain.decision_engine import DecisionEngine

from app.ai.brain_integration.v63.brain_retrieval_connector import BrainRetrievalConnector



class IntelligentBrain:


    def __init__(self):

        self.retrieval = BrainRetrievalConnector()

        self.reasoning = ReasoningEngine()

        self.decision = DecisionEngine()



    def think(
        self,
        agent_id,
        mission
    ):


        context = self.retrieval.retrieve_context(
            agent_id,
            mission
        )


        reasoning = self.reasoning.reason(
            context["context"]
        )


        decision = self.decision.make_decision(
            reasoning
        )


        return {

            "agent_id": agent_id,

            "mission": mission,

            "context": context,

            "reasoning": reasoning,

            "decision": decision,

            "status": "completed",

            "timestamp": datetime.utcnow().isoformat()

        }