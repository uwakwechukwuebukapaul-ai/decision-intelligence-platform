class ResponseGenerator:
    """
    Generates analyst-friendly responses.
    """

    def generate(
        self,
        context
    ):

        intent = context.get(
            "intent"
        )


        if intent == "investigation":

            return {

                "response":
                    "Starting investigation workflow.",

                "next_steps": [

                    "Collect evidence",

                    "Analyze indicators",

                    "Map attacker behavior",

                    "Recommend response"

                ]

            }


        if intent == "explanation":

            return {

                "response":
                    "Providing investigation reasoning.",

                "analysis":

                    "Decision based on collected intelligence, risk scoring, and historical patterns."

            }


        if intent == "recommendation":

            return {

                "response":
                    "Recommended security actions.",

                "actions": [

                    "Contain affected asset",

                    "Review indicators",

                    "Validate threat scope"

                ]

            }


        return {

            "response":
                "Sentinel Copilot analyzed the request.",

            "intent":
                intent

        }