from .copilot_model import CopilotResponse
from .security_reasoner import SecurityReasoner
from .conversation_memory import ConversationMemory



class CopilotEngine:
    """
    Sentinel DNA AI SOC Copilot.

    Acts as an AI security analyst assistant.
    """


    def __init__(self):

        self.reasoner = SecurityReasoner()

        self.memory = ConversationMemory()



    def ask(
        self,
        question
    ):

        analysis = self.reasoner.analyze(
            question
        )


        answer = (
            "Security analysis completed. "
            "Review recommended investigation steps."
        )


        response = CopilotResponse(

            answer=answer,

            confidence=
                analysis["confidence"],

            recommendations=
                analysis["recommendations"],

            reasoning=
                analysis

        )


        result = response.to_dict()



        self.memory.remember(

            question,

            result

        )


        return result