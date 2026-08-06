"""
Sentinel DNA

IOC Timeline Engine

Responsibilities:

- Track investigation events
- Maintain chronological history
- Provide explainable investigation flow
"""


from __future__ import annotations

from datetime import datetime
from uuid import uuid4



class TimelineEngine:
    """
    Investigation timeline manager.
    """


    def __init__(
        self,
    ):

        self.events = []



    def add_event(
        self,
        event_type: str,
        details: dict,
        source: str = "ioc-intelligence",
    ) -> dict:
        """
        Add investigation event.
        """


        event = {

            "event_id": str(
                uuid4()
            ),

            "timestamp": datetime.utcnow().isoformat(),

            "event_type": event_type,

            "source": source,

            "details": details,

        }


        self.events.append(
            event
        )


        return event



    def get_timeline(
        self,
    ) -> list:
        """
        Return ordered investigation timeline.
        """


        return sorted(
            self.events,
            key=lambda event: event["timestamp"],
        )



    def build_from_intelligence(
        self,
        intelligence: dict,
    ) -> list:
        """
        Generate timeline from IOC intelligence result.
        """


        self.add_event(
            "ioc_detected",
            {
                "indicator": intelligence.get(
                    "indicator"
                )
            }
        )


        if intelligence.get(
            "risk"
        ):

            self.add_event(
                "risk_analysis_completed",
                intelligence["risk"],
            )


        if intelligence.get(
            "reputation"
        ):

            self.add_event(
                "reputation_analysis_completed",
                intelligence["reputation"],
            )


        if intelligence.get(
            "mitre_mapping"
        ):

            self.add_event(
                "mitre_mapping_completed",
                {
                    "techniques":
                        intelligence["mitre_mapping"]
                },
            )


        return self.get_timeline()