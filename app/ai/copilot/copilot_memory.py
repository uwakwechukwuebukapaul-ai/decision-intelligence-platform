"""
Sentinel DNA Copilot Memory

Uses investigation history.
"""


class CopilotMemory:


    def summarize(
        self,
        intelligence: dict,
    ) -> dict:


        memory = intelligence.get(
            "memory",
            []
        )


        return {

            "previous_investigations":
                len(memory),

            "historical_match":
                len(memory) > 0,

        }