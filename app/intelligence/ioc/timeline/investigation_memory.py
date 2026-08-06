"""
Sentinel DNA

Investigation Memory Engine

Responsibilities:

- Preserve AI investigation context
- Store reasoning chain
- Support future AI Copilot memory
"""


from __future__ import annotations

from datetime import datetime



class InvestigationMemory:
    """
    Investigation context memory manager.
    """


    def __init__(
        self,
    ):

        self.memory = {}



    def create_memory(
        self,
        indicator: str,
    ) -> dict:
        """
        Create investigation memory object.
        """


        context = {

            "indicator": indicator,

            "created_at":
                datetime.utcnow().isoformat(),

            "actions": [],

            "reasoning_chain": [],

            "analyst_notes": [],

        }


        self.memory[indicator] = context


        return context



    def record_action(
        self,
        indicator: str,
        action: str,
        reasoning: str,
    ) -> dict:
        """
        Record AI investigation action.
        """


        if indicator not in self.memory:

            self.create_memory(
                indicator
            )


        entry = {

            "action": action,

            "reasoning": reasoning,

            "timestamp":
                datetime.utcnow().isoformat(),

        }


        self.memory[indicator]["actions"].append(
            entry
        )


        self.memory[indicator]["reasoning_chain"].append(
            reasoning
        )


        return entry



    def add_note(
        self,
        indicator: str,
        note: str,
    ) -> dict:
        """
        Add analyst note.
        """


        if indicator not in self.memory:

            self.create_memory(
                indicator
            )


        self.memory[indicator]["analyst_notes"].append(
            {
                "note": note,
                "timestamp":
                    datetime.utcnow().isoformat(),
            }
        )


        return self.memory[indicator]



    def get_memory(
        self,
        indicator: str,
    ) -> dict | None:
        """
        Retrieve investigation memory.
        """


        return self.memory.get(
            indicator
        )