class PromptManager:
    """
    Creates structured AI investigation prompts.
    """

    def build(self, question):

        return {

            "system_role":
                "You are Sentinel DNA AI SOC Copilot",

            "objective":
                "Assist SOC analysts with security investigations",

            "question":
                question,

            "requirements":
                [
                    "Analyze evidence",
                    "Explain findings",
                    "Recommend actions"
                ]

        }