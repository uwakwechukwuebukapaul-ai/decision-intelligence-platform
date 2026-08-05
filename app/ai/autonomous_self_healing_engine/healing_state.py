"""
Self Healing State Model

Tracks autonomous recovery actions.
"""

from datetime import datetime, UTC



class HealingState:


    def __init__(
        self,
        component=None,
        status="healthy"
    ):

        self.component = component

        self.status = status

        self.created_at = (
            datetime.now(
                UTC
            ).isoformat()
        )


    def to_dict(self):

        return {

            "component":
                self.component,

            "status":
                self.status,

            "created_at":
                self.created_at

        }