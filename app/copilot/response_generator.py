from datetime import datetime


class ResponseGenerator:
    """
    Generates final Copilot responses.
    """

    def generate(
        self,
        conversation,
        analysis,
        investigation
    ):

        return {

            "answer":

                "Sentinel DNA Copilot analyzed the request and generated investigation guidance.",


            "intent":
                conversation["intent"],


            "recommendations":
                analysis["recommendations"],


            "investigation_plan":
                investigation["investigation_steps"],


            "confidence":
                92,


            "timestamp":
                datetime.utcnow().isoformat()

        }