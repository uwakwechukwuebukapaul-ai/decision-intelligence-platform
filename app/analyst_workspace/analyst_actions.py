"""
Analyst Action Tracking
"""

from datetime import datetime


class AnalystActionTracker:


    def __init__(self):

        self.actions = []



    def record(
        self,
        indicator: str,
        action: str,
        analyst: str = "ai-agent",
    ):


        event = {

            "indicator": indicator,

            "action": action,

            "analyst": analyst,

            "timestamp":
                datetime.utcnow().isoformat(),

        }


        self.actions.append(
            event
        )


        return event



    def history(self):

        return self.actions