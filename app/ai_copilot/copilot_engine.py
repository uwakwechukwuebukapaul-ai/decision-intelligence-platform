from datetime import datetime

from .query_interpreter import QueryInterpreter
from .security_reasoner import SecurityReasoner
from .investigation_assistant import InvestigationAssistant
from .response_assistant import ResponseAssistant
from .knowledge_engine import KnowledgeEngine
from .copilot_memory import CopilotMemory


class CopilotEngine:
    """
    Sentinel DNA AI Security Copilot Engine.
    """


    def __init__(self):

        self.query = QueryInterpreter()

        self.reasoner = SecurityReasoner()

        self.investigator = InvestigationAssistant()

        self.response = ResponseAssistant()

        self.knowledge = KnowledgeEngine()

        self.memory = CopilotMemory()



    def assist(
        self,
        request
    ):

        interpretation = self.query.interpret(
            request
        )


        reasoning = self.reasoner.reason(
            request
        )


        investigation = self.investigator.assist(
            request
        )


        response = self.response.recommend(
            request
        )


        result = {

            "status": "completed",

            "request": request,

            "interpretation": interpretation,

            "reasoning": reasoning,

            "investigation": investigation,

            "response": response,

            "created_at": datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return result