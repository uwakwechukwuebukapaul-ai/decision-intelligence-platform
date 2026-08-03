from datetime import datetime

from app.ai.brain.context_processor import ContextProcessor
from app.ai.brain.reasoning_engine import ReasoningEngine
from app.ai.brain.decision_engine import DecisionEngine



class AgentBrain:


    def __init__(self):

        self.context_processor = ContextProcessor()

        self.reasoning_engine = ReasoningEngine()

        self.decision_engine = DecisionEngine()



    def think(

        self,

        agent_id,

        mission,

        memories=None

    ):


        context = self.context_processor.process(

            mission,

            memories

        )


        reasoning = self.reasoning_engine.reason(

            context

        )


        decision = self.decision_engine.decide(

            reasoning

        )


        return {

            "agent_id":
                agent_id,


            "context":
                context,


            "reasoning":
                reasoning,


            "decision":
                decision,


            "status":
                "completed",


            "timestamp":
                datetime.utcnow().isoformat()

        }