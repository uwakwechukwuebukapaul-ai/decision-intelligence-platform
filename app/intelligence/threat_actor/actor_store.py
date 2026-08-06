"""
Sentinel DNA - Threat Actor Memory Store
"""


from datetime import datetime





class ThreatActorStore:


    def __init__(self):

        self.records = []




    def save(
        self,
        result: dict,
    ):


        result["stored_at"] = (
            datetime.utcnow()
            .isoformat()
        )


        self.records.append(
            result
        )


        return result





    def get_all(self):

        return self.records