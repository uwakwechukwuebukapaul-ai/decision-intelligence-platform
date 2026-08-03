from datetime import datetime

from .conversation_engine import ConversationEngine
from .prompt_manager import PromptManager
from .analyst_assistant import AnalystAssistant
from .investigation_helper import InvestigationHelper
from .response_generator import ResponseGenerator
from .copilot_memory import CopilotMemory



class SOCCopilot:
    """
    Sentinel DNA AI SOC Copilot.

    Connects SOC analysts with:
    - Reasoning
    - Investigation
    - Recommendations
    - Memory
    """

    def __init__(self):

        self.conversation = ConversationEngine()

        self.prompt = PromptManager()

        self.assistant = AnalystAssistant()

        self.investigator = InvestigationHelper()

        self.response = ResponseGenerator()

        self.memory = CopilotMemory()



    def ask(self, question):


        conversation = self.conversation.process(
            question
        )


        prompt = self.prompt.build(
            question
        )


        analysis = self.assistant.assist(
            question
        )


        investigation = self.investigator.guide(
            question
        )


        result = self.response.generate(
            conversation,
            analysis,
            investigation
        )


        result["prompt"] = prompt

        result["created_at"] = (
            datetime.utcnow()
            .isoformat()
        )


        self.memory.store(
            result
        )


        return result