"""
Sentinel DNA - Investigation Timeline Engine

Maintains chronological SOC investigation events.

Compatibility:
- InvestigationTimeline
- Timeline
"""


from __future__ import annotations


from datetime import datetime





class InvestigationTimeline:
    """
    Investigation timeline manager.

    Stores:
    - investigation stages
    - analyst actions
    - system events
    """



    def __init__(
        self,
    ):

        self.events = []



    def add_event(
        self,
        stage: str,
        message: str,
    ) -> dict:
        """
        Add timeline event.
        """

        event = {

            "stage": stage,

            "message": message,

            "timestamp":
            datetime.utcnow().isoformat(),

        }


        self.events.append(
            event
        )


        return event





    def get_events(
        self,
    ) -> list:
        """
        Return timeline history.
        """

        return self.events





    def all(
        self,
    ) -> list:
        """
        Compatibility alias.
        """

        return self.events





# Backward compatibility

Timeline = InvestigationTimeline