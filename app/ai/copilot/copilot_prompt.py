"""
Sentinel DNA Copilot Prompt Builder
"""


class CopilotPromptBuilder:


    def build(
        self,
        intelligence: dict,
    ) -> str:


        indicator = intelligence.get(
            "indicator",
            "unknown"
        )


        return (

            f"Investigate indicator {indicator}. "

            "Review risk, campaigns, "
            "threat actors, graph relationships "
            "and provide SOC analyst guidance."

        )