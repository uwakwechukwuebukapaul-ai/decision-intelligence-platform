from .query_parser import QueryParser
from .response_generator import ResponseGenerator
from .investigation_assistant import InvestigationAssistant


class CopilotEngine:
    """
    Central Sentinel DNA AI Copilot.

    Connects analyst queries
    with Sentinel intelligence.
    """

    def __init__(self):

        self.parser = QueryParser()

        self.generator = ResponseGenerator()

        self.investigator = InvestigationAssistant()



    def ask(
        self,
        query
    ):

        context = self.parser.parse(
            query
        )


        response = self.generator.generate(
            context
        )


        return {

            "query":
                query,

            "context":
                context,

            "response":
                response,

            "copilot_status":
                "active"

        }



    def investigate(
        self,
        incident
    ):

        return self.investigator.investigate(
            incident
        )