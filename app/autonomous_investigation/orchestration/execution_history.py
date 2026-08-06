"""
Sentinel DNA Investigation Execution History
"""


from datetime import datetime
from uuid import uuid4



class ExecutionHistory:


    def __init__(self):

        self.events = []



    def record(
        self,
        event: str,
        details: dict | None = None,
    ):


        entry = {

            "event_id":
                str(uuid4()),


            "event":
                event,


            "details":
                details or {},


            "timestamp":
                datetime.utcnow().isoformat(),

        }


        self.events.append(entry)


        return entry



    def all(self):

        return self.events