"""
Sentinel DNA Decision Repository

Persistence layer for AI decisions.
"""



from datetime import datetime



class DecisionRepository:



    def __init__(self):

        self.decisions = []



    def save(
        self,
        decision: dict
    ):

        decision["created_at"] = (
            datetime.utcnow()
            .isoformat()
        )


        self.decisions.append(
            decision
        )


        return decision



    def list_all(self):

        return self.decisions