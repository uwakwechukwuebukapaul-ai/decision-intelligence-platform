"""
Knowledge State Model

Tracks autonomous knowledge lifecycle.
"""

from datetime import datetime, UTC


class KnowledgeState:


    def __init__(
        self,
        knowledge_id=None,
        state="active"
    ):

        self.knowledge_id = knowledge_id

        self.state = state

        self.created_at = (
            datetime.now(
                UTC
            ).isoformat()
        )


    def to_dict(self):

        return {

            "knowledge_id":
                self.knowledge_id,

            "state":
                self.state,

            "created_at":
                self.created_at

        }